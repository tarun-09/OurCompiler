#!/usr/bin/env python3
import sys
import os
from Sansam.Run import run

def main():
    if len(sys.argv) != 2:
        print("Usage: sansam <filename.sans>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    if not filename.endswith('.sans'):
        print("Error: File must have .sans extension")
        sys.exit(1)
        
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    
    try:
        # First copy the file content to trail.txt since that's what the interpreter expects
        script_dir = os.path.dirname(os.path.abspath(__file__))
        trail_file = os.path.join(script_dir, "Sansam", "trail.txt")
        
        with open(filename, 'r', encoding='utf-8') as source, \
             open(trail_file, 'w', encoding='utf-8') as dest:
            content = source.read()
            dest.write(content)
        
        # Now run the program
        result, error = run(trail_file, content)
        
        if error:
            print(error.as_string())
            sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
