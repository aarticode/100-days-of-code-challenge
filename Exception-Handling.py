#Python try...except
#try….. except blocks are used in python to handle errors and exceptions.
# The code in try block runs when there is no error.
#If the try block catches the error, then the except block is executed.
#Example1
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
  for i in range(1, 11):
      print(f"{int(a)} X {i} = {int(a)*i}")
except:
     print("Invalid  Input!")
     print("Some imp lines of code")
     print("End of program")

#Example2

try:
    num = int(input("Enter an integer: "))
    a = [6,4]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error")

#Handling Multiple Exceptions:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Exiting the program.")

# Handling exceptions in dictionaries, tuples, sets, and lists

try:
    # Dictionary
    my_dict = {"a": 1, "b": 2}
    value1 = my_dict["c"]
except KeyError:
    print("Key not found in dictionary.")

try:
    # Tuple
    my_tuple = (1, 2, 3)
    value2 = my_tuple[3]
except IndexError:
    print("Index out of range for tuple.")

try:
    # Set
    my_set = {1, 2, 3}
    my_set.remove(4)
except KeyError:
    print("Element not found in set.")

try:
    # List
    my_list = [1, 2, 3]
    value3 = my_list[3]
except IndexError:
    print("Index out of range for list.")

# Handling exceptions with variables and functions

try:
    # Variable
    x = 10 / y  # Assuming y is not defined
except NameError:
    print("Variable not defined.")

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        return result

divide(10, 0)

# Handling exceptions in loops
my_list = [1, 2, 3]
for item in my_list:
    try:
        print(item / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero in loop.")


