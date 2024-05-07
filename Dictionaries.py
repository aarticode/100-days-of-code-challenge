#Python Dictionaries
#Dictionaries are ordered collection of data items.
# They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)


#I. Accessing single values:
#There is also a method called get() that will give you the same result:
#Get the value of the "model" key:
dic= {'name':'Karan', 'age':19, 'eligible':True}
print(dic['name'])
print(dic.get('eligible'))

#II. Accessing multiple values:
#The values() method will return a list of all the values in the dictionary.
dic= {'name':'Sahil', 'age':24, 'eligible':True}
print(dic.values())

#III. Accessing keys:
#We can print all the keys in the dictionary using keys() method.
dic= {'name':'Mohit', 'age':24, 'eligible':True}
print(dic.keys())

#IV. Accessing key-value pairs:
#We can print all the key-value pairs in the dictionary using items() method.
dic= {'name':'Akasnksha', 'age':23, 'eligible':True}
print(dic.items())

#Dictionary Methods
#Dictionary uses several built-in methods for manipulation.They are listed below
#update()
#The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

dic= {'name':'Rohit', 'age':19, 'eligible':True}
dic.update({'age':21})
dic.update({'DOB':2003})
print(dic)

#Removing items from dictionary:
#There are a few methods that we can use to remove items from dictionary.
#clear():
#The clear() method removes all the items from the list.
dic = {'name':'Ajali', 'age':19, 'eligible':True}
dic.clear()
print(dic)

#pop():
#The pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name':'Abhishek', 'age':29, 'eligible':True}
info.pop('eligible')
print(info)

#popitem():
#The popitem() method removes the last key-value pair from the dictionary.
info = {'name':'Mohit', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)


#del:
#we can also use the del keyword to remove a dictionary item.
info = {'name':'Aarti', 'age':23, 'eligible':True, 'DOB':2000}
del info['eligible']
print(info)

#If key is not provided, then the del keyword will delete the dictionary entirely.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
#print(info)

#Dictionary Methods
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1)

