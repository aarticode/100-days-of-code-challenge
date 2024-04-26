#What are strings?
#In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters
#Example
name = "Aarti"
friend = "Rohan"
anotherFriend = 'Mohit'

#Multiline Strings
#If our string has multiple lines, we can create them like this:
apple = '''He said, 
Hi Aarti
hey I am good
"I want to eat an apple'''

print("Hello, " + name)
# print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
#Looping through the string
#We can loop through strings using a for loop like this:
print("Lets use a for loop\n")
for character in apple:
    print(character)

#String as an array
#A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

#Example:
pie = "ApplePie"
print(pie[:5])
print(pie[6]) #returns character at specified index


# This method of specifying the start and end index to specify a part of a string is called slicing.

#Slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

#Loop through a String:
#Strings are arrays and arrays are iterable. Thus we can loop through strings.

#Example:
alphabets = "ABCDE"

for i in alphabets:
    print(i)