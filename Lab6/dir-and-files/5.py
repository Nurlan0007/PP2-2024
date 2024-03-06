def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write("%s\n" % item)

# Specify the file path and the list to write
file_path = 'some.txt'
data_list = ['apple', 'banana', 'cherry', 'date']

try:
    write_list_to_file(file_path, data_list)
    print(f"The list has been written to the file '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")