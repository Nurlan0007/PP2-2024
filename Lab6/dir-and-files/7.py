def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            contents = source.read()
            destination.write(contents)
        print(f"Contents of '{source_file}' have been successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"The file '{source_file}' was not found.")

source_file_path = 'some.txt'
destination_file_path = 'destination.txt'

copy_file_contents(source_file_path, destination_file_path)