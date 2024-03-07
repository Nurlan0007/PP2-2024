import os

def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path_to_test = "C:\\Users\\Nurlan\\Desktop\\PP2_2024"
test_path(path_to_test)