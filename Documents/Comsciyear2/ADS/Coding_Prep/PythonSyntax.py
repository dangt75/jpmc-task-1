# Declare variable and print statement

hello = "Hello World"
print(hello)


# Concatenation string

name = "Toan"
# 1st way
print(hello + " " + name)
# 2nd way
print(hello, name)


# Lists

# Declaration

list = ["bike", "car", "motor"]

# Get the element
first_e = list[0]
last_e = list[-1]

# Making a numerical list
numList = [x**2 for x in range(1,11)]

# Slicing and copying list
slice_list = list[:2]
copy_list = list[:]

#Adding an element to end of list

list.append("truck")

#Inserting element to a particular position

list.insert(0,"plane")

#Deleting element by either position or value

del list[-1]

list.remove("bike")

#Popping element if need to use remove element

remove_item = list.pop(2)

#Sorting function for list

list.sort() # will sort array permanently
new_list = sorted(list) # will sort and return new array sorted but keep original one unchanged

#Tuple 

tuple = ("sleep", "happy") # likes list but cannot change individual value when already set up

tuple = ("go", "study") # can overwrite all elements

#Dictionary

dictionary = {"color": "green", "points": 5, "target" : "Goggle"}

print(dictionary["color"]) # Getting the associated value from key

#Using get function to get value associated from key

color = dictionary.get("color")
target = dictionary.get("target")

print(target)

#Adding key-value pair to the dictionary
dictionary["offer"] = 0

#Removing key-value pair to the dictionary
del dictionary["offer"] 

#Looping through each key-value pair

for key, value in dictionary.items():
    print(key, ":", value)

#Looping through key set
for key in dictionary.keys():
    print(key)

#Looping through value set
for value in dictionary.values():
    print(value)


