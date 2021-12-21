#Manipulating List

#List Full
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print (fam)
#This prints "['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]"

#List in a List 00
fam2 = [["liz", 1.73], ["emma", 1.68], ["mom", 1.71], ["dad", 1.89]]
print (fam2)
#This prints "[['liz', 1.73], ['emma', 1.68], ['mom', 1.71], ['dad', 1.89]]"

#List in a List 01
fam = [1.73, 1.68, 1.71, 1.89]
fam2 = [fam, 2.87, 1.22]
print (fam2)
#This prints "[[1.73, 1.68, 1.71, 1.89], 2.87, 1.22]"

#List in a List 02
fam = [1.73, 1.68, 1.71, 1.89]
fam2 = [fam[2], 2.87, 1.22]
print (fam2)
#This prints "[1.71, 2.87, 1.22]"

#List in a List 03
fam2 = [["liz", 1.73], ["emma", 1.68], ["mom", 1.71], ["dad", 1.89]]
print (fam2[2])
#This prints "['mom', 1.71]"

#List Slicing
print (fam[3:5])
#Remember, in list [start : end] start is inclusive BUT end is exclusive.

print (fam[:4]) #This prints the list items from 0-3. (Since, end is exclusive).

print (fam[4:]) #This prints the list items from 4-last. (Since, start is inclusive).

#Changing List Elements
fam [0:2] = ["Lisa", 1.74]
print (fam)

fam [7] = 1.86
print (fam)

#Adding and Removing Elements
fam_ext0 = ["me", 1.79] + fam
print (fam_ext0)

fam_ext1 = fam + ["me", 1.79]
print (fam_ext1)

del (fam_ext1[2])
print (fam_ext1)

fam_ext1[7] = "SK"
print (fam_ext1)

#Behind the Scenes
x = ["a", "b", "c"]
y = x #Here, writing 'y = x' is a must. If use, 'x = y' then 'y' remains undefined.
y [1] = "z"
print (y)
print (x)

#List can be printed in the following ways
x = ["a", "b", "c"]

y = x
print (y)

y = list(x)
print (y)

y = x[:]
print (y)
#Primarily, the three above methods output the same thing. BUT, the show hasn't finished. Let's see!

x = ["a", "b", "c"]

y = list (x) #Give attention
y [1] = "z"
print (x)
print (y)
#This program DOES NOT manipulate x and print "['a', 'b', 'c']"

x = ["a", "b", "c"]

y = x [:] #Give attention
y [1] = "z"
print (x)
print (y)
#This program also DOES NOT manipulate x and print "['a', 'b', 'c']"

x = ["a", "b", "c"]

y = x #Give attention
y [1] = "z"
print (x)
print (y)
#This program MANIPULATES x and prints "['a', 'z', 'c']"

#So, manipulation BECOMES DIFFERENT based on the method used to define 'y'. Check the line with "#Give attention" comment.

#Another, Self Testing Exercise:
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

print (fam)
del fam [0:2]

print (fam)
fam [7] = 1.86

print (fam)

del fam [0:2]

print (fam)

fam2 = ["liz", 1.73] + fam

print (fam2)

fam2 [0:2] = ["lisa", 1.77]

print (fam2)

#Round
#Round function prints the rounded number upto the defined point starting from 0 at the left to right position.
#Round a number to a given precision in decimal digits (default 0 digits).
#It rounds decimal digits from 6-9 but NOT 0-5
print (round(1.7525,3))
#The program above outputs 1.752 NOT 1.753 as we do in regular works.
print (round(1.7526,3))
#The program above outputs 1.753.

#However, this functions works differently based on the position of the numbers.
#For example,
#print (round(1.7525,3))
#Outputs 1.752 WITHOUT rounding it to 1.753.

#Difference between prining all the listed items in a list using loop and direct method.

fam = [1.73, 1.68, 1.71, 1.89]

#Loop Way
for i in range (4):
    print (fam[i])
#Above one prints vertically like below (vertically):
#1.73
#1.68
#1.71
#1.89

#Direct Way
print (fam[:])
#This one prints vertically like below (horizontally):
#[1.73, 1.68, 1.71, 1.89]
#Note the brackets here in this method.

#Index 00
#To know the position (index) of a item in a list:
fam = [1.73, 1.68, 1.71, 1.89]
print (fam.index(1.89))
#print (list_name.index(querry))
#This program outputs "3" as the position of 1.89.

#Index also works in non-list items. See below:
f = "J", "T", "S0", "S1", "S2"
print (f.index("S0"))
#This program outputs "2" as the position of "S0".

#Index also works in a single item to find a single item.
sis = "zarin"
print(sis.index("n"))
#This program outputs "4" as the position of "n".

#Objects of different types can have methods with the same name:
#Take the index method. It's available for both strings and lists.
#If used on a string, it returns the index of the letters in the string;
#But, if used on a list, it returns the index of the element in the list.
#This means that, based on the type of the object, the methods behave differently.

#Capitalize
sis = "zarin"
print (sis.capitalize())
#This program capitalize the first letter of the string and outputs "Zarin"

#Upper
sis = "zarin"
print (sis.upper())
#This program capitalize all letters of the string and outputs "ZARIN"

#Lower
sis = "ZARIN"
print (sis.lower())
#This program de-capitalize all letters of the string and outputs "zarin"

#Count 00
f = "J", "T", "S0", "S1", "S2"
print (f.count("S1"))
#'Count' counts the how many times an item has appeared in a list.
#This program outputs 1. Since, "S1" appeared only one time in f.

#Count 01
fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
print (fam.count(1.73))
#This program outputs 1. Since, 1.73 appeared only one time in f.
print (fam.count("1.73"))
#This program outputs 0. Since, 1.73 appeared as a number but NOT as a string in f.
#Same thing goes with indexing too.

#Replace 00
s = "ZMS"
sister = s.replace ("MS", "arin") #Case sensitive. Using "ms" does NOT do anything. Because, there is NO "ms" in s variable.
#To repleace, use "variable_name.replace ("WHAT to replace", "WITH WHAT to replace")"
print (sister)
#This one prints "Zarin"

#Reversing 00
name = "sifat kashif" [::-1]
print (name)
#This one prints "fihsak tafis"

#Reversing 01
fam = [1.73, 1.7525, 1.71, 1.89] [::-1]
print (fam)
#This one prints "[1.89, 1.71, 1.7525, 1.73]"
#Here, first colon is for slicing as we know. And, second one is for defining the range, maybe?

#Reversing 02
fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
fam.reverse()
print (fam)

#Reversing 03
fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
fam.reverse()
print (fam)
#This one prints "[1.89, 'dad', 1.71, 'mom', 1.68, 'emma', 1.73, 'liz']"
#reverse () modifies the list on which it is applied.
#Nothe that, 'str' object has no attribute 'reverse'.

#Length 00
name = "sifat kashif"
print (len(name))
#This one prints 12. The length of the string.

#Length 01
fam = [1.73, 1.68, 1.71, 1.89]
print (len (fam))
#This one prints 4. The length of the list.

#Maximum
fam = [1.73, 1.7525, 1.71, 1.89]
print (max(fam))
#This one prints 1.89. The maximum number in the list.

#Minimum
fam = [1.73, 1.7525, 1.71, 1.89]
print (min(fam))
#This one prints 1.71. The minimum number in the list.

#Help
print(help(print))
#This one prints the built-in help instructions.
#Can be used with the name of functions in parentheses to know about those functions.
#For example,
print(help(bool))
#Prints help on class bool.

#Python functions, like type, max and round, that you can use like this.
#type(fam)
#This outputs "list"
#There's also methods, which are functions that are specific to Python objects.
#Based on the type of the Python object you're dealing with, you can use different methods and they behave differently.
#You can use methods on the objects with the dot notation. For example:
#fam.index("dad")
#This outputs "6"

#Append 00
fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

fam.append ("me")
fam.append (1.76)

print (fam)
#This outputs "['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89, 'me', 1.76]"
#Append modifies the list.
#Append can add exactly one item at a time.