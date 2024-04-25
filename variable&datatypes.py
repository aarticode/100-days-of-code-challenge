#What is a variable?
#Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc
# Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
x = 5
y = "Aarti"
print(x)
print(y)

x = 4       # x is of type int
x = "Sahil" # x is now of type str
print(x)

#These are four variables of different data types.
a = 1
b = True
c = "Akash"
d = None
b = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#What is a Data Type?
#Data type specifies the type of value a variable holds.
# This is required in programming to do various operations without causing an error.
#In python, we can print the type of any operator using type function:
a1 = 9
print(a + a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))

#4. Sequenced data: list, tuple
#list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.
#Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

#Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses.
# Tuples are immutable and can not be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

#5. Mapped data: dict
#dict: A dictionary is an unordered collection of data containing a key:value pair.
#The key:value pairs are enclosed within curly brackets.
thisdict = dict(name = "Aarti", age = 23, country = "india")
print(thisdict)