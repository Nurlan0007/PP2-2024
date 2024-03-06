def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)


file_path = 'some.txt'

try:
    line_count = count_lines(file_path)
    print(f"The file '{file_path}' has {line_count} lines.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
