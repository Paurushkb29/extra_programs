#Write a python program to perform read and write operation on a file using user defined module. 

# main.py

import file_operations

# File to read from and write to
filename = "example.txt"

# Content to write to the file
content_to_write = "Hello, this is some content written to the file."

# Write content to the file
write_result = file_operations.write_file(filename, content_to_write)
print(write_result)

# Read content from the file
read_result = file_operations.read_file(filename)
print("Content read from the file:")
print(read_result)
