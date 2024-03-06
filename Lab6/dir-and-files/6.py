import string
import os

file_names = [f"{char}.txt" for char in string.ascii_uppercase]

for file_name in file_names:
    with open(file_name, 'w') as file:
        file.write(f"This is file {file_name}\n")

print("Files A.txt through Z.txt have been created.")