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

#Finally Clause
#The finally code block is also a part of exception handling.
# When we handle exception using the try and except block, we can include a finally block at the end.
# The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")

x = func1()
print(x)


#Raising Custom errors
#In python, we can raise custom errors by using the raise keyword.
a = int ( input ("Enter  any value   between 5 and  9"))

if (a<5 or a>9):
    raise  ValueError("Value should be between 5 and 9")

#Example2
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")


#Defining Custom Exceptions
#In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

class CustomError(Exception):
    """A custom exception class."""
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)

# Example usage
def divide(x, y):
    if y == 0:
        raise CustomError("Division by zero is not allowed")
    return x / y

try:
    result = divide(10, 0)
    print("Result of division:", result)
except CustomError as e:
    print("Error:", e)



#Example
 #class InsufficientFundsError(Exception):
    """Exception raised when an account has insufficient funds for a transaction."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance {balance}, Attempted Transaction {amount}")


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


# Main program
def main():
    initial_balance = 1000
    account = BankAccount(initial_balance)

    try:
        print("Current balance:", account.balance)
        withdrawal_amount = float(input("Enter withdrawal amount: "))
        remaining_balance = account.withdraw(withdrawal_amount)
        print("Withdrawal successful.")
        print("Remaining balance:", remaining_balance)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except InsufficientFundsError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
