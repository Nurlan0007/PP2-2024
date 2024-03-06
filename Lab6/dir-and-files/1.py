import os

def list_dir_files(path):
    # List only directories
    print("Directories:")
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            print(name)

    # List only files
    print("\nFiles:")
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            print(name)

    # List all directories and files
    print("\nAll directories and files:")
    for name in os.listdir(path):
        print(name)

# Specify the path
path = "C:\\Users\\Nurlan\\Desktop\\PP2_2024"
list_dir_files(path)