# Diyar Parwana, Linköping
# Run the file deepscan.py path
# Let the path of the memory device to be the first argument 

import os
import sys

# File types...
FILE_SIGNATURES = {
    'JPEG': b'\xFF\xD8\xFF\xE0',
    'PNG': b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
    
}

def find_files(device_path):
    with open(device_path, 'rb') as device:
        while True:
           # To be able to read 4KB at a time
            chunk = device.read(4096)  
            if not chunk:
                break
            for file_type, signature in FILE_SIGNATURES.items():
                if signature in chunk:
                    print(f"Found potential {file_type} file at position {device.tell()}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: deepscan.py <device_path>")
        sys.exit(1)

    device_path = sys.argv[1]
    find_files(device_path)
