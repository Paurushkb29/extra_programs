#Write a Python program to perform the Fibonacci series using the recursion function.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(count):
    if count <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci series:")
        for i in range(count):
            print(fibonacci(i), end=" ")

# Get user input for the number of terms
terms = int(input("Enter the number of terms for Fibonacci series: "))
print_fibonacci_series(terms)
