#f-string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Aarti"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
name = 'Aarti Chouhan'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

#Docstrings in python
#Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

#Example
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)


#Python doc attribute
#Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute.
# We can later use this attribute to retrieve this docstring.

#Example
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)


def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)


#PEP 8
#PEP 8 is a document that provides guidelines and best practices on how to write Python code.
# It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

#PEP stands for Python Enhancement Proposal, and there are several of them.
# A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.
#The Zen of Python
#Long time Pythoneer Tim Peters succinctly channels the BDFL’s guiding principles for Python’s design into 20 aphorisms, only 19 of
# which have been written down.


import this



