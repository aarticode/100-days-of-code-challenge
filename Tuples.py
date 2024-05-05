#Python Tuples
#Tuples are ordered collection of data items.
# They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

#I. Positive Indexing:
#As we have seen that tuple items have index, as such we can access items using these indexes.
tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])



#II. Negative Indexing:
#Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.
tup = (1, 2, 76, 342, 32, "green", True)
print(tup[-4])
print(tup[-1])
print(tup[-2])

#III. Check for item:
#We can check if a given item is present in the tuple. This is done using the in keyword.

Class = ("Aarti", "Chanchal", "Rohit", "Mohit", "Aman")
if "Aman" in Class:
    print("Aman is present.")
else:
    print("Aman is absent.")

Class = ("Aarti", "Chanchal", "Rohit", "Mohit", "Aman")
if "Kapil " in Class:
    print("Kapil is present.")
else:
    print("Kapil is absent.")


#Example: Printing elements within a particular range:
tup = (1, 2, 76, 342, 32, "green", True)
tup2 = tup[1:4]    #using positive indexes
print(tup2)
tup2 = tup[-6:-2]  #using negative indexes
print(tup2)

#Example: Printing all element from a given index till the end
tup = ("Aarti", "Chanchal", "Rohit", "Mohit", "Aman" ,"Sahil", "Aakash")
tup2 = tup[4:]   #using positive indexes
print(tup2)

#Example: printing all elements from start to a given index
tup2 = tup[:-4]  #using negative indexes
print(tup2)

#Example: Print alternate values:
tup = ("Aarti", "Chanchal", "Rohit", "Mohit", "Aman" ,"Sahil", "Aakash")
tup2 = tup[::2]
print(tup2)

tup2 = tup[-6:-1:2]
print(tup2)

#Example: printing every 3rd consecutive withing given range

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])


#Manipulating Tuples
#Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)


#we can directly concatenate two tuples without converting them to list.
tuple1 = (1,2,3,"Aarti")
tuple2 = ("chouhan",5,6)
tuple3= tuple1+ tuple2
print(tuple3)


#Tuple methods
#As tuple is immutable type of collection of elements it have limited built in methods.
#count() Method
#The count() method of Tuple returns the number of times the given element appears in the tuple.

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)

#index() method
#The Index() method returns the first occurrence of the given element from the tuple.
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)