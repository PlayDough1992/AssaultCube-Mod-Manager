import os
import sys
import py_compile
import marshal

def compile_mod(file_path):
    """
    Compile a Python mod file (.py) into AssaultCube Mod format (.acm)
    ACM format contains:
    - Mod name (from filename)
    - Compiled bytecode
    - Version info
    """
    # Extract mod name from file path (remove .py extension)
    mod_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Get path to output .acm file
    output_path = os.path.join('dist', 'mods', f'{mod_name}.acm')
    
    try:
        # Create bytecode by compiling the Python source
        # This generates a code object but doesn't write to disk
        code = py_compile.compile(file_path, doraise=True)
        
        # Read the compiled bytecode from the .pyc file
        with open(code, 'rb') as f:
            # Skip first 16 bytes (pyc header containing timestamp and size info)
            f.seek(16)
            # Load the actual code object from the remaining bytes
            code_obj = marshal.load(f)
        
        # Create our custom .acm format data
        mod_data = {
            'name': mod_name,          # Mod identifier
            'code': code_obj,          # Compiled bytecode
            'version': '1.00'          # Mod format version
        }
        
        # Ensure dist/mods directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write the .acm file using marshal to serialize the data
        # Marshal is used because it can handle code objects
        with open(output_path, 'wb') as f:
            marshal.dump(mod_data, f)
            
        print(f"[+] Compiled {mod_name} -> {output_path}")
        return True
        
    except Exception as e:
        print(f"[-] Failed to compile {mod_name}: {e}")
        return False
    finally:
        # Clean up temporary .pyc file if it exists
        if code and os.path.exists(code):
            os.unlink(code)

def main():
    """
    Main entry point for mod compiler
    Usage: python mod_compiler.py [mod_file.py]
    If no file specified, compiles all .py files in mods/ directory
    """
    # Get mod files to compile
    if len(sys.argv) > 1:
        # Specific file provided
        mod_files = [sys.argv[1]]
    else:
        # No file specified - compile all mods in mods/ directory
        mods_dir = 'mods'
        if not os.path.exists(mods_dir):
            print(f"[-] Mods directory not found: {mods_dir}")
            return False
            
        # Get all .py files except __init__.py
        mod_files = [
            os.path.join(mods_dir, f) 
            for f in os.listdir(mods_dir)
            if f.endswith('.py') and f != '__init__.py'
        ]
    
    # Track compilation success
    success = True
    
    # Compile each mod file
    for mod_file in mod_files:
        if not os.path.exists(mod_file):
            print(f"[-] Mod file not found: {mod_file}")
            success = False
            continue
            
        if not compile_mod(mod_file):
            success = False
    
    return success

if __name__ == '__main__':
    # Run compiler and exit with appropriate status code
    sys.exit(0 if main() else 1)