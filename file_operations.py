#Write a python program to perform read and write operation on a file using user defined module. 

# file_operations.py

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    return "Write operation successful."

