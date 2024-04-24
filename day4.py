#Day 4 - Taking User Input in python
#In python, we can take user input directly by using input() function.This input function gives a return value as
# string/character hence we have to pass that into a variable
a = input("Enter your name: ")
print("My name is", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x  + y)
print(int(x) + int(y))

#How can we prompt the user for multiple inputs at once?
#You can prompt the user for multiple inputs by separating them with commas inside the input() function. For example:
name, age = input("Enter your name and age separated by a comma: ").split(',')
print("Hello,", name)
print("You are", age, "years old.")

#How can we handle cases where the user input might cause errors, such as attempting to convert a non-numeric input to an integer?
#You can use exception handling with try and except blocks to handle potential errors gracefully. For example:
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a valid number.")






