#Set 00
#'Set' removes duplicates and prints the output 'once' for every unique items.
kids = {"alice", "bob", "charlie","mike", "bob", "mike"}
print (kids)
#This program outputs "{'alice', 'mike', 'charlie', 'bob'}"
#Note that, set disregards the serial of appearance.
#That means, instead of printing "{'alice', 'bob', 'charlie', 'mike'}", it prints "{'alice', 'mike', 'charlie', 'bob'}"

#Index 00
n = "sifu is a boy"
print(n.index (" "))
print (n [n.index(" "):])
#This program outputs as follows:
#5
# is a boy

#Multi-line Commenting 00
'''
Example text
'''
"""
Example text
"""

#Strip 00
n = " sifu is a boy "
print (n.strip())
#This program outputs "sifu is a boy" removing the spaces at the start and end of the string.

#Packages 00
#To see the packages installed in you machine:
#pip freeze

#Try-Except 00
#print (10/0)
#This program outputs an error message "ZeroDivisionError: division by zero"
try:
    print (10/0)
except:
    print("An exception occurred") 
#This program outputs "An exception occurred" as coded in the above lines.
