#Python Sets
#Sets are unordered collection of data items. They store multiple items in a single variable.
# Set items are separated by commas and enclosed within curly brackets {}.
# Sets are unchangeable, meaning you cannot change items of the set once created.
#Sets do not contain duplicate items
sets = {"Python", 19, False, 5.9, 19}
print(sets)

#Accessing set items:
#Using a For loop
#You can access items of set using a for loop.
s= {2, "True", 4, 2,"false" ,6.1, 0, 1}
# Create an empty set
empty_set = set()
for value in s:
  print(value)


#Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set
# Check the type of the variable
Aarti = set()
print (type(Aarti))

#Joining Sets
#Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.
#I. union() and update():
#The union() and update() methods prints all items that are present in the two sets.
# The union() method returns a new set whereas update() method adds item into the existing set from another set.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


#Update
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 5,6}
set1.update(set2)
print(set1)


#II. intersection and intersection_update():
#Keep ONLY the duplicates
#The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry", "mango"}
set2 = {"google", "microsoft", "apple" ,"cherry"}
set1.intersection_update(set2)
print(set1)

#III. symmetric_difference and symmetric_difference_update():
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)


#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
#Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#IV. difference() and difference_update():
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
#Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


#Set Methods
#There are several in-built methods used for the manipulation of set.They are explained below
#isdisjoint():
#The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
#Return True if no items in set x is present in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issuperset():
#The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))


#issubset():
#The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
cities= {"UP", "Chennai", "Delhi" "Haryana"}
cities2= {"Delhi","Haryana"}
print(cities2.issubset(cities))

#add()
#If you want to add a single item to the set use the add() method.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)



#update()
#If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)


#remove()/discard()
#We can use remove() and discard() methods to remove items form list.
cities = {"UP", "Haryana", "Chennai", "Delhi"}
cities.remove("UP")
print(cities)

#pop()
#This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
cities = {"UP", "Haryana", "Chennai", "Delhi"}
item = cities.pop()
print(cities)
print(item)


#del
#del is not a method, rather it is a keyword which deletes the set entirely.
cities = { "UP", "Haryana", "Chennai" ,"Delhi"}
del cities
#print(cities)


#clear():
#This method clears all items in the set and prints an empty set.
cities = { "UP", "Haryana", "Chennai" ,"Delhi"}
cities.clear()
print(cities)

#Check if item exists
#You can also check if an item exists in the set or not.
student= {"Karan", "Sahil" ,"Rohit", 101 ,5.9}
if "Karan" in student:
    print("Karan is present.")
else:
    print("Karan is absent.")




import string

def count_word_frequency(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()

    # Create an empty set to store unique words
    unique_words = set(words)

    # Count the frequency of each unique word using sets
    word_frequency = {}
    for word in unique_words:
        word_frequency[word] = words.count(word)

    return word_frequency

def display_word_frequency(word_frequency):
    print("Word Frequency:")
    for word, frequency in sorted(word_frequency.items()):
        print(f"{word}: {frequency}")

def main():
    text = input("Enter a piece of text: ")
    word_frequency = count_word_frequency(text)
    display_word_frequency(word_frequency)

if __name__ == "__main__":
    main()
