#write a simple Python program to print all possible combination of characters.

from itertools import permutations

characters = input("Enter the string\n") # Define the characters
perms = permutations(characters) # Generate all permutations of the characters
print(list(map(''.join, perms))) # Print permutations as a list


# from itertools import permutations

# def print_combinations(characters):
#     # Generate all permutations of the characters
#     perms = permutations(characters)
#     print(perms)
#     # Print each permutation
#     for perm in perms:
#         print(''.join(perm))

# # Example usage:
# characters = input("Enter the string\n")
# print_combinations(characters)



# def print_combinations(characters, prefix='', n=None):
#     if n is None:
#         n = len(characters)
#     if n == 0:
#         print(prefix)
#         return
#     for char in characters:
#         print_combinations(characters, prefix + char, n - 1)

# # Example usage:
# characters = input("Enter the string\n")#'abc'
# print_combinations(characters)
