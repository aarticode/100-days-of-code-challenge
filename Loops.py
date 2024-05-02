#The for Loop
#for loops can iterate over a sequence of iterable objects in python.
# Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

#Example: iterating over a string:

name = 'Rohit'
for i in name:
    print(i)
    if(i == "r"):
        print("This first word in name")

#Example: iterating over a list:

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

string = "hello"
for a  in string:
    print(a)

#Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)


#range():
#What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?
#Here, we can use the range() function.

#Example:
for k in range(5):
  print(k +1)


#Example2
for k in range(6, 10):
   print(k)

#Python while Loop
#As the name suggests, while loops execute statements while the condition is True.
# As soon as the condition becomes False,
#the interpreter comes out of the while loop.
i = int(input("Enter the number: "))
print(i)
while(i<=10):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

#Else with While Loop
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

#How to emulate do while loop in python?
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
#Break statement
#The break statement enables a program to skip over a part of the code.
# A break statement terminates the very loop it lies within.
start = 10
end = 20

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(f"The first prime number in the range {start}-{end} is:", num)
            break


#Break statement
#The break statement enables a program to skip over a part of the code.
# A break statement terminates the very loop it lies within.
for i in range(5):
    if (i == 5):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 5 == 0):
        break

for i in range(1, 101, 1):
    print(i, end=" ")
    if (i == 10):
        break
    else:
        print("BREAK")
print("Thank you")


#Continue Statement
#The continue statement skips the rest of the loop statements and causes the next iteration to occur.
for i in [2,3,4,6,8,9,11,10,12,14,15,16,17,18,19,20]:
    if (i%2!=0):
        continue
    print(i)

for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)


