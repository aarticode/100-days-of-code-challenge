#Python Recursive Function
#In Python, we know that a function can call other functions.
# It is even possible for the function to call itself.
# These types of construct are termed as recursive functions.
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))
# Driver Code
print(factorial(6))

#Recursion to print a star pattern, such as a triangle, square, or any other shape. Let's start with a simple example of printing a triangle of stars:
def print_triangle(rows):
    if rows > 0:
        print_triangle(rows - 1)  # Print the triangle with one less row
        print('*' * rows)         # Print the current row of stars
print_triangle(5)

# Pyramid pattern of stars using recursion:
def print_pyramid(rows, current_row=0, spaces=0):
    if current_row < rows:
        # Print spaces before the stars
        print(' ' * (rows - current_row - 1) + '*' * (2 * current_row + 1))
        print_pyramid(rows, current_row + 1)
print_pyramid(5)



#The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones. It typically starts with 0 and 1, and the subsequent numbers are generated by adding the previous two. The sequence begins:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# f(n) = f(n-1) + f(n-2)
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)


# Quick Quiz: Write a program to print the Fibonacci sequence
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Taking input from the user for the number of terms
n = int(input("Enter the number of terms: "))

# Generating and printing the Fibonacci series
fib_series = fibonacci(n)
print("Fibonacci Series:")
print(fib_series)



#Question: Write a Python function to generate the Fibonacci series up to a given number n.
def fibonacci_series(n):
    fib_series = [0, 1]  # Initialize with the first two Fibonacci numbers
    while fib_series[-1] + fib_series[-2] <= n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series

# Example usage:
n = 20  # Generate Fibonacci series up to 20
print(fibonacci_series(n))



def fibonacci(n):
    fib_series = [0, 1]  # Initialize with the first two Fibonacci numbers
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series

# Example usage:
n = 30  # Generate the first 8 Fibonacci numbers
print(fibonacci(n))




def fibonacci(n):
    fib_series = [0, 1]  # Initialize with the first two Fibonacci numbers
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series[-1] if n > 1 else fib_series[0]

# Prompting the user to input a number
n = int(input("Enter the value of n to find the nth Fibonacci number: "))

# Calculate the nth Fibonacci number
result = fibonacci(n)

# Display the result
print(f"The {n}th Fibonacci number is: {result}")



