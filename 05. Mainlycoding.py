#Tuple 00
a = ("a", "b", "w", "z")
print (type (a))
#This program outputs "<class 'tuple'>"

#Set 00
a = {"a", "b", "w", "z"}
print (type (a))
#This program outputs "<class 'set'>"

#Set 01
a = {"a", "b", "a", "z", "w", "z"}
print (a)
#This program outputs "{'a', 'w', 'b', 'z'}"
#Set outputs the elements in the set WITH REMOVING DUPLICATES AND WITHOUT MAINTAINING ANY SEQUENCE.

#Data Types 00
x = 1 #int
y = 2.8 #float
z = 1j #complex #Note the letter 'j' at the end.
print (type(x))
print (type(y))
print (type(z))
#This program outputs:
#<class 'int'>
#<class 'float'>
#<class 'complex'>
#Note that, when using complex number, it is required to add 'j' at the end of the number.

#Data Type Conversion 00
x = 1 #int
y = 2.8 #float
z = 1j #complex

#Conversion from int to float:
print ("Conversion from int to float:")
print (x)
print (type(x))

a = float (x)
print (a)
print (type(a))
print ("")

#Conversion from float to int:
print ("Conversion from float to int:")
print (y)
print (type(y))

b = int (y)
print (b)
print (type(b))
print ("")

#Conversion from int to complex:
print ("Conversion from int to complex:")
print (x)
print (type(x))

c = complex (x)
print (c)
print (type(c))

#This program outputs as follows:
#Conversion from int to float:
#1
#<class 'int'>
#1.0
#<class 'float'>

#Conversion from float to int:
#2.8
#<class 'float'>
#2
#<class 'int'>

#Conversion from int to complex:
#1
#<class 'int'>
#(1+0j)
#<class 'complex'>

#List 00
shoppingList = ["apple", "banana", "mango", "orange", "pen", "melon", "book"]
print (shoppingList[2:5])
print (shoppingList[(shoppingList.index("mango")):(shoppingList.index("melon"))])
#This program outputs:
#['mango', 'orange', 'pen']
#['mango', 'orange', 'pen']
#But, using different methods.

#Manipulating List 00
shoppingList = ["apple", "banana", "mango", "orange", "pen", "melon", "book"]
shoppingList [1] = "cherry"
print (shoppingList)
#This program outputs "['apple', 'cherry', 'mango', 'orange', 'pen', 'melon', 'book']"

#Manipulating List 01
shoppingList = ["apple", "banana", "mango", "orange", "pen", "melon", "book"]
shoppingList [1:3] = "comic", "berry"
print (shoppingList)
#This program outputs "['apple', 'comic', 'berry', 'orange', 'pen', 'melon', 'book']"

#Tuple 00
sampleTuple = ("apple", "banana", "mango")
print(sampleTuple[2])
#This program outputs: "mango"

#Tuple 01
sampleTuple = ("apple", "banana", "mango")
print(sampleTuple)
simpleTuple (1) = "b" #Program breaks at this line.
#This program outputs: "SyntaxError: can't assign to function call"
#Tuple is like a list. But, here it is not possible to manipulate items.

#String 00
sample0 = "This is a string"
print(sample0)
#This program outputs: "This is a string"
sample1 = '''This is
a string'''
print(sample1)
#This program outputs: This is
#a string

'''Similar to using multi
line comments'''

#Set 00
demoSet = {"apple", "banana", "mango", "banana", "cherry", "mango"}
print(demoSet)
#This program outputs: "{'banana', 'apple', 'cherry', 'mango'}"
#Surprisingly, outputs of this program varies every time it get run.
#WITHOUT MAINTAINING ANY FIXED ORDER.

#Dictionary 00
d = {'apple':2,'mango':4}
print(d)
#This program outputs: "{'apple': 2, 'mango': 4}"
print (d["apple"])
#This program outputs: 2
d["apple"] = 3
print (d["apple"])
#Like List, the above method can be used to manipulate dictionary values too.
#Then the program outputs: 3
#Here, 'apple' is a key and '2' is a value.

#Comparison Operation 00
x = 20
y = 7
print (x==y)
print (x!=y)
print (x>y)
print (x<y)
print (x>=y)
print (x<=y)
#This program outputs as follows:
#False
#True
#True
#False
#True
#False

#True has value 1 and False has value 0.
print ((x==y) + (x!=y))
#This program outputs 1
print ((x==y) + (x==y))
#This program outputs 0

#Logical Operation 00
x = True
y = False
print(x and y)
print(x or y)
print(not x)
#This program outputs:
#False
#True
#False

#Asignment Operation 00
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c)

c *= a
print ("Line 3 - Value of c is ", c) 

c /= a 
print ("Line 4 - Value of c is ", c) 

c  = 2
c %= a
print ("Line 5 - Value of c is ", c)

c **= a
print ("Line 6 - Value of c is ", c)

c //= a
print ("Line 7 - Value of c is ", c)

#This program outputs as below:
#Line 1 - Value of c is  31
#Line 2 - Value of c is  52
#Line 3 - Value of c is  1092
#Line 4 - Value of c is  52.0
#Line 5 - Value of c is  2
#Line 6 - Value of c is  2097152
#Line 7 - Value of c is  99864

#Note:
#a += b means a = a + b
#a -= b means a = a - b
#a *= b means a = a * b
#a /= b means a = a / b
#a %= b means a = a % b
#a **= b means a = a ** b

#Adding Items In A List 00
numbers = [23, 1, 12, 18, 21, 10, 28, 98, 22]
sum = 0
for i in numbers:
    #print (i)
    sum = sum + i
print (sum)
#This program outputs 233. Sum of the items in the list.

#While Loop 00
#Using 'While loop' is useful when it is unknown that how many times it is required for a program to iterate.
sum = 0
k = int(input())
i = k + 1
n = 0
while n < i:
    sum = sum + n
    n = n + 1    
print (sum)
#This program outputs 210

#Alternatively, it is possible to use <= in the while condition to avoid the "i = k + 1" part of this program.
sum = 0
k = int(input())
#i = k + 1 (Avoided)
n = 0
while n <= k: #Used <= at the place of <. So, it is also possible to use k directly.
    sum = sum + n
    n = n + 1    
print (sum)
#This program outputs 210

#Break 00
for val in "Bangla":
    if val == "l":
        break
    print(val)

print("The end")
#This program outputs as follows:
#B
#a
#n
#g
#The end
#Break is used when it is required to exit a loop in a certain condition or state.

#Continue 00
for val in "Bangla":
    if val == "l": #Continue actually skips this item and goes to the next one.
        continue
    print(val)

print("The end")
#This program outputs as follows:
#B
#a
#n
#g
#a
#The end
#Continue is used when it is required to skip a item and continue to the next item in the loop after skipping.
#For quick recall, just think: "Continue = Skip"

#Function 00
def add (a,b):
    return (a+b)
print (add(11,9))
#This program outputs "20"
#Here, the structure is as follows:
#def function_name(parameters):
    #statement(s)
        #return

