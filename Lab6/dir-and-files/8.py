import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.R_OK):
            try:
                os.remove(file_path)
                print(f"The file '{file_path}' has been deleted.")
            except Exception as e:
                print(f"An error occurred while deleting the file: {e}")
        else:
            print(f"The file '{file_path}' is not accessible for reading.")
    else:
        print(f"The file '{file_path}' does not exist.")

file_path_to_delete = 'some.txt'
delete_file(file_path_to_delete)