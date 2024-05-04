#Example of List Comprehension
marks = [3, 5, 6, "Aarti", True, 6, 7 , 2, 32, 345, 23]
if "6" in marks:
   print("Yes")
else:
   print("No")
#same thing applies for strings as well!
if "Aa" in "Aarti":
    print("Yes")

#Example 2: Accepts items which have more than 4 letters
items = ["apple", "banana", "orange", "grape", "kiwi", "melon", "lemon"]
selected_items = [item for item in items if len(item) > 4]
print(selected_items)

#Example 3: Accepts items with the small letter “o” in the new list
items = ["apple", "banana", "orange", "grape", "kiwi", "melon", "lemon"]
selected_items = [item for item in items if 'o' in item]
print(selected_items)


#Example: printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

#Example: printing all element from a given index till the end
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

#Example: printing all elements from start to a given index
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

#Example: Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

#Example: printing every 3rd consecutive value withing a given range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# Using positive indexes
print(animals[3:7])


#Appending an Element to a List:
l = ["cat", "dog", "bat", "mouse"]
l.append("pig")
print(l)

#Sorting a List:
l = [3, 1, 4, 2,10,9,8,7,6,0]
l.sort()
print(l)

#Reverse a list
l = [1, 2, 3, 4,7,5,8,9]
l.reverse()
print(l)

#Finding the Index of an Element:
l = ["cat", "dog", "bat", "mouse"]
index = l.index("bat")
print(index)

#Counting Occurrences of an Element
l = [1, 2, 3, 4, 1, 1]
count = l.count(1)
print(count)

#Copying a List:
l = [1, 2, 3]
m = l.copy()
print(m)

colors = ["voilet", "green", "red", "blue"]
colors.insert(1, "green")
print(colors)

#Inserting an Element at a Specific Index:
colors = ["voilet", "green", "red", "blue"]
colors.insert(1, "green")
print(colors)

#Extending a List with Another List:
l = [1, 2, 3]
m = [4, 5, 6]
l.extend(m)
print(l)

#Concatenating two lists:
#You can simply concatenate two lists to join two lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)

#Using the 'extend()' method:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)










