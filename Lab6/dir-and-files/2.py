import os

def check_path_access(path):
    # Check if the path exists
    exists = os.path.exists(path)
    print(f"Path exists: {exists}")

    # Check if the path is readable
    if exists:
        readable = os.access(path, os.R_OK)
        print(f"Path is readable: {readable}")
    else:
        print("Path is not readable: path does not exist")

    # Check if the path is writable
    if exists:
        writable = os.access(path, os.W_OK)
        print(f"Path is writable: {writable}")
    else:
        print("Path is not writable: path does not exist")

    # Check if the path is executable
    if exists:
        executable = os.access(path, os.X_OK)
        print(f"Path is executable: {executable}")
    else:
        print("Path is not executable: path does not exist")

# Specify the path to check
path_to_check = "C:\\Users\\Nurlan\\Desktop\\PP2_2024"
check_path_access(path_to_check)