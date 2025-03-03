import hashlib
import os
import sys
import time

def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                sha1.update(chunk)
        return sha1.hexdigest()
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except PermissionError:
        print("Error: Permission denied.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 integrity.py <file> [directory]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    save_dir = sys.argv[2] if len(sys.argv) == 3 else os.path.expanduser("~/integrity")
    os.makedirs(save_dir, exist_ok=True)
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    sha1_hash = calculate_sha1(file_path)
    
    result = f"[{timestamp}] - [{file_path}] - [sha1:{sha1_hash}]\n"
    print(result.strip())
    
    result_file = os.path.join(save_dir, "integrity.txt")
    with open(result_file, "a") as f:
        f.write(result)
    
    os.chmod(result_file, 0o600)  # Only user can read and write
    print(f"Integrity check completed. Result stored in {result_file}")

if __name__ == "__main__":
    main()
