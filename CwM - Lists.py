'''
CwM - Lists
'''

#
#
# READ ME: This is the main variable calls you will need to use for the following sections to execute properly. (Sections 1.0, and 1.2)!
#
#

# indices   0        1       2
#names = ['James', 'Mary', 'David', 'James']



# Section 1.0
# Here we will understand how to use the methods, ".append", ".pop", and ".insert"
'''

print(names)
names.append('Linda')                           # added to Index 3 w/ .append method.
print('Adding Linda to the List:', names[3])    # Added a little flair to it.
print(names)                                    # Printing Updated List up to this point.
names.pop()                                     # .pop removes from the end of the list.
print('Removing Linda from the List:', names)   # "Removing" a little flair xd.
print(names)                                    # Printing Updated List up to this point.
names.insert(1, 'Susan')                        # Inserting 'Susan' at Index 1 for the List "names".
print(names[1])                                 # Checking if 'Susan' appears at Index 1 as instructed to Python.
print('Now inserting Susan at Index 1', names)  # Adding a little flair again.
names.pop(1)                                    # Popping from Index 1, to remove 'Susan'.
print('Removing Susan from Index 1', names)     # Adding a little flair... again. 
'''



# Section 1.1
# Here we will use numbers instead for our List.
'''
numbers = []
#numbers.append(10)                             # This is a very inneficient way to add values to a numbers list, so let's use an alt. method.
for num in range(100):
    if num > 0 and num % 2 == 0:                # Modulus (% sign) 2 would make it even numbers only (in the printed List).
#    if num > 0 and num % 3 == 0:               # Modulus 3 will make it odd numbers only (in the printed List).
        numbers.append(num)
print(numbers)
'''




# Section 1.2
# We will be going back to the "names" List and understand the ".clear", ".remove", and "" method.

# ".clear" method.
'''
print(names)
names.clear()                                   # This will clear the items from the List.
print(names)
'''


# ".index" method to check specific Index position/ location.
'''
val = names.index('James')                      # Try typing in different names from the "names" List.
print(val)                                      # Should print '0', '1', '2', dependent on item name from List.
'''


# ".remove" method to remove a value from the List.
'''
names.remove('James')                           # Remove method works on the values, instead of the keys. It will ONLY remove ONE VALUE from the List.
print(names)                                    # This will print the remainder of the values from the List.
'''


# ".pop" method to pop a value from the List.
'''
val = names.pop()                               # You can specify which index to pop from the List by using a index number in the parentheses, but it cannot be a str.
print(val)                                      # Should print the item in whatever data-type you set it as (str, int, flt, etc.), dependent on item name from List.
'''

# "len" method.
'''
print(len(names))                               # This will print out the number of values from the List.
'''

# ".count" method.
'''
print(names.count('James'))                     # This will count the amount of the same values are present from the List.
'''




# Section 1.3
# We will use 2 lists this time.

'''
names = []
boys = ['James', 'David', 'Michael', 'Richard'] # This is the boys List.
girls = ['Mary', 'Linda', 'Carol']              # This is the girls List.

# There is an easier way to use this "for" loop function in a smaller bloc of code...!
"""
for name in boys:
    names.append(name)
for name in girls:
    names.append(name)
print(names)
"""

names.extend(boys)                              # Extends one value ("names" List) of the List with another List ("boys" List).
names.extend(girls)                             # Extends "names" List with "girls" List.
print(names)
print(boys)
print(girls)
'''

# Section 1.4
# We will learn the ".sort" method as it is important/ commonly used in computers.
'''
names = ['Mary', 'Linda', 'Carol', 'James', 'David', 'Michael', 'Richard']          # Notice how the names/ strings are not in Alpha order...

names.sort()
print(names)
'''

# Section 1.5
# Iterating Strings to print out one character after the other until end of string (like from our "Free-Style" section from "CwM - Loops.py").
'''
characters = []
greeting = 'Good Morning'
for char in greeting:                           # "char" CHECKS in variable "greeting" until end of string.
    if char not in characters:                  # If a char IS NOT in the characters List
        characters.append(char)                 # ".append" the "char" from "greeting" variable to the "characters" List..
        print(characters)
print(characters)
'''

# Section 1.6
# Checking if said str is in List with "in" funct.
'''
names = ['James', 'Lisa', 'Mark', 'Carol']
print('james' in names)                         # This will print out as 'False' if it's not properly case-sensitive.
'''




'''
Free-Style~
'''

# I'm going to keep this as quick and simple as possible because I want to move onto the next lecture.
#Caesar_List = ['Apples', 'Bread', 'Cilantro']


Caesar_List = []                                # Blank List for now.
grocery_items = ['Apples', 'Bread', 'Cilantro', "Caesar's Signature Spice <3"]
for items in grocery_items:
    if Caesar_List != grocery_items[-1]:
        Caesar_List.append(items)
        print('Updated, Caesar_List:')
        print(Caesar_List)
print('End of Loop.')