#if-else Statements
a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators
# >, <, >=, <=, ==, !=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")



#elif Statements
#Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

#nested-if
num = 18
if (num > 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

# Checking a student's grade based on their score
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your grade is:", grade)



#If ... Else in One Line
#There is also a shorthand syntax for the if-else statement that can be used when
# the condition being tested is simple and the code blocks to be executed are short. Here's an example:
a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")
c = 9 if a>b else 0
print(c)


#Example
a=2
b=330
print ("A") if a>b else print ("B")


#Example
#One line if else statement, with 3 conditions:
a = 33000
b = 33023

print("A") if a > b else print("=") if a == b else print("B")
c = 10 if a > b else  0
