#Function Arguments and return statement
#Default arguments:
#We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.
def calculatevalue(a, b):
    mean = ( a *b ) /(a +b)
    print(mean)
def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
a = 9
b = 8
isGreater(a, b)
calculatevalue(a, b)
c = 7
d = 8
isGreater(c, d)
calculatevalue(c, d)


#Calling a function:
#We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

#Example:
def name(fname, lname):
    print("Hello,", fname, lname)
name("AARTI", "CHOUHAN")

#Default arguments:
#We can provide a default value while creating a function.
# This way the function assumes a default value even if a value is not provided in the function call for that argument.
#Example
def average(a=9, b=1):
  print("The average is ", (a + b ) / 2)

average(8)

#Example
def name(fname, mname = "john", lname = "Aagrwaal"):
    print("Hello,", fname, mname, lname)
name("Amy")

#Keyword arguments:
#We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
#Example:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Mohan", lname = "Singh", fname = "Radhe")

#Example
def average(a, b,c=1):
  print("The average is ", (a + b +c) / 2)
average(5,6)

#Required Arguments:
def add(x, y):
    return x + y

result = add(3, 5)
print(result)

#Arbitrary Arguments:
#While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
#Example:
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is: ", sum / len(numbers))
average(5, 6,7,1)

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))


#Keyword Arbitrary Arguments:
#While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.
#Example:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "mohan", lname = "singh", fname = "Radhe")

def sum_numbers(**numbers):
    total = 0
    for key, value in numbers.items():
        print(f"{key}: {value}")
        total += value
    print("Total:", total)

# Example usage
sum_numbers(one=1, two=2, three=3, four=4, five=5)



#return Statement
#The return statement is used to return the value of the expression back to the calling function.
#Example
def average(*numbers):

    sum = 0
    for i in numbers:
        sum = sum + i
        return sum / len(numbers)
c=average(2, 3,4,1)
print(c)







