#Multiple Assignment 00
a, b, c, d, e = 0, 1.5, "check", True, 2j
print (a, b, c, d, e)
print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
#This program outputs as below:
#0 1.5 check True 2j
#<class 'int'>
#<class 'float'>
#<class 'str'>
#<class 'bool'>
#<class 'complex'>

#It is possible to assign multiple types of values to multiple variables in a single line.
#But, it is not possible to output the types of multiple variables in a single line. Like below:
#print (type(a,b,c,d))
#This program outputs: TypeError: type() takes 1 or 3 arguments

#Floor Division 00
print(7//2)
print(-11//3)
print(-11//-3)
print(11//-3)
#This program outputs as below:
#3
#-4
#3
#-4
#For posoitive numbers, floor division rounds to the bigger integer.
#And for negative numbers, floor division rounds to the smaller integer.

#Boolean 00
x = True
y = False

print ("OR")
print (x or y)
print (x | y)

print ("AND")
print (x and y)
print (x & y)

print ("NOT")
print (not y)
#This program outputs as below:
#OR
#True
#True
#AND
#False
#False
#NOT
#True

#Boolean 01
x = 5
y = 6
z = 7

print(x < y)
print(x == 5)
print(y == 4)
print((x + y) > z)
print((x + y) <= z)
print(x != y)
print((x < y) & (y == 6))
print((x < y) & (z !=y))
print((x > y) | ( z != y))
print((x > y) & (z != y))
print((x < y) & (z == y))
print((x < y) | (z == y))

#This program outputs as follows:
#True
#True
#False
#True
#False
#True
#True
#True
#True
#False
#False
#True

#Number System 00
#Bin can be used to see the value of an operator
x = 99
print(bin(x))
print(oct(x))
print(hex(x))
print(int(x))

#This program outputs as below:
#0b1100011
#0o143
#0x63
#99
#Here, the first two letters states the base. For example:
#0b for Binary
#0o for Octal
#0x for Hexadecimal
#But the decimal does not include any base identifier.

#Bitwise Operation 00
a = 9
b = 10
c = a and b
print (c)
c = a & b
print (c)

#The above two lines outputs different values:
#10
#8

#NEED CLARIFICATION AND ADDTIONAL STUDY!

#Binary Operation 00
#Binary OR
# |
#Binary AND
# &
#Binary XOR
# ^
#Binary NOT
# ~

#NEED CLARIFICATION AND ADDTIONAL STUDY!

#Identity Operator 00
a = 20
b = 20
if a is b:
    print("a and b have same identity")
else:
    print("a and b do not have same identity")
#This program outputs: "a and b have same identity"

#Identity Operator 01
a = 20
b = 2
if a is not b:
    print("a and b do not have same identity")
else:
    print("a and b have same identity")
#This program outputs "a and b do not have same identity"

#When same value get assigned to two different variables, computer uses same single memory location for those two variables.
#Identity operators are used to check whether two variables are in same memory location or not.

#Identity Operator 02
a = 20
b = 20
print (id(a))
print (id(b))
#This program outputs:
#1941695280
#1941695280
#Note that, the ids are same.

a = 10
b = 30
print (id(a))
print (id(b))
#This program outputs:
#1941695120
#1941695440
#Note that, the ids are different.

#However, the memory ids may get changed on different times.
#But, the same values have similar id and different values have dissimilar ids.

#List 00
box = ["Python", 3.1416, 911]
print (type(box))
print (type(box[0]))
print (type(box[1]))
print (type(box[2]))
#This program outputs as below:
#<class 'list'>
#<class 'str'>
#<class 'float'>
#<class 'int'>
#It is possible to insert and find different types of data in a list.

#List 01
rainbow_colors = ["red", "green", "blue"]
rc = rainbow_colors
nrc = rc + ["yellow"]
print (rc)
print (id(rc))
print (nrc)
print (id(nrc))
#This program outputs:
#['red', 'green', 'blue']
#['red', 'green', 'blue', 'yellow']
#With a DISSIMILAR memory location. (Omitted in this comment part)

#List 02 Append
rainbow_colors = ["red", "green", "blue"]
rc = rainbow_colors
print (id(rainbow_colors))
print (id(rc))
rc.append ("yellow")
print (rc)
print (rainbow_colors)
#This program outputs:
#['red', 'green', 'blue', 'yellow']
#['red', 'green', 'blue', 'yellow']
#With a SIMILAR memory location. (Omitted in this comment part)

#List 03 Append
colors = ["red", "green", "blue"]
print (id(colors))
colors.append("yellow")
print (colors)
print (id(colors))
#This program outputs:['red', 'green', 'blue', 'yellow'] with a SIMILAR memory location. (Omitted in this comment part)

#List 04 Append Multiple Error
#However, it is NOT possible to add multiple items at a time using append.
#colors = ["red", "green", "blue"]
#print (id(colors))
#colors.append("yellow", "orange")
#print (colors)
#print (id(colors))
#The above program outputs: "TypeError: append() takes exactly one argument (2 given)"

#List 05 Append Multiple
colors = ["red", "green", "blue"]
print (id(colors))
colors.append(["yellow", "orange"])
print (colors)
print (id(colors))
'''The above program outputs: ['red', 'green', 'blue', ['yellow', 'orange']] making a (sub)list of ['yellow', 'orange'],
while keeping a similar memory location.
However, it is possible to use 'extend' function to fix this. See #List 06.'''

#List 06 Extend
colors = ["red", "green", "blue"]
print (id(colors))
colors.extend(["yellow", "orange"])
print (colors)
print (id(colors))
'''The above program outputs: ['red', 'green', 'blue', 'yellow', 'orange']
with a SIMILAR memory location. (Omitted in this comment part)'''

#In a nutshell, extend requires using "[]" append does NOT.
#Append adds one item at a time. Extend adds multiple.
#If append is used to add multiple items using "[]", it makes a list in a list. But, extend does NOT make that list in a list.

#Len 00
colors0 = ["red", "green", "blue", "orange", "yellow", "indigo", "violet", 12, 4]
colors1 = "Hi learner!"
print (len(colors0))
print (len(colors1))
#This program outputs:
#9
#11
#Len is a function. And, functions are used without dot notation.

#Count 00
numbers = [4,6,1,3,8,5,7,9,2]
c = numbers.count(6)
print (c)
#This program outputs: 1. (Since 6 was appeared one time in the list).

#Note that, where len function counts the total number of letters in a variable,
#Count method counts how many time(s) a item has appeared in the variable.

#Remove 00
colors = ["red", "green", "blue", "orange", "yellow", "indigo", "violet"]
colors.remove ("red")
print (colors)
#This program outputs: ['green', 'blue', 'orange', 'yellow', 'indigo', 'violet']

#Del 00
colors = ["red", "green", "blue", "orange", "yellow", "indigo", "violet"]
del colors[0]
print (colors)
#This program outputs: ['green', 'blue', 'orange', 'yellow', 'indigo', 'violet']

#Del 01
colors = ["red", "green", "blue", "orange", "yellow", "indigo", "violet"]
del colors[2:5]
print (colors)
#This program outputs: ['red', 'green', 'indigo', 'violet']

#Del 02
numbers = [4,6,1,3,8,5,7,9,2]
del numbers [:]
print (numbers)
#This program outputs: []. (Since all items in the list are deleted).
#However, the list is still existing.
#numbers.clear() do the same too. See #Clear 00

#Del 03
numbers = [4,6,1,3,8,5,7,9,2]
del numbers
print (numbers)
#But, this program outputs: "NameError: name 'numbers' is not defined"
#Since, del has deleted the whole list varible named numbers.

#Note that, Remove can be used with item name. OTOH, Del can be used with index number.
#Remove() takes exactly one argument
#So, Remove can be used to remove one item per command. [Like Append]
#But, in Del, it is possible to delete a range of multiple items. [Like Extend]
#Del is a function (like "print") but remove is an attribute of list.
#So, del is used directly but remove is used with dot notation).

#Pop 00
colors = ["red", "green", "blue", "orange", "yellow", "indigo", "violet"]
pop = colors.pop(2)
print (colors)
print (pop)
#Pop can be used to remove an item and assign it to a new variable.
#This program outputs as below:
#['red', 'green', 'orange', 'yellow', 'indigo', 'violet']
#blue

#Pop 01
colors = ["red", "green", "blue", "orange", "yellow", "indigo", "violet"]
pop = colors.pop() #No parameter given in ()
print (colors)
print (pop)
#This program outputs as below:
#['red', 'green', 'blue', 'orange', 'yellow', 'indigo']
#violet
#If there is no parameter passed in the pop, it removes the last item and assigns that value in a new variable.
#Pop can be used (with dot notation) to remove one item per command. Like, append and remove.
#Mind that, pop method uses index number UNLIKE remove method that uses item value.

#Reverse 00
f = ['c', 'b', 'a', 'd', 'f', 'e']
#del (f[:])
f.reverse()
print (f)
#This program outputs: ['e', 'f', 'd', 'a', 'b', 'c']

#Sort 00
numbers = [4,6,1,3,8,5,7,9,2]
numbers.sort()
print (numbers)
#This program outputs: "[1, 2, 3, 4, 5, 6, 7, 8, 9]"
#As default, sort method sorts in ascending order.

#Sort 01
numbers = [4,6,1,3,8,5,7,9,2]
numbers.sort(reverse=True) #For descending order
print (numbers)
#This program outputs: "[9, 8, 7, 6, 5, 4, 3, 2, 1]"
#As default, sort method sorts in ascending order.
#"reverse=True" is passed in the parameter () to sort in descending order.

#Sort 02
alphabet = ["c", "b", "a", "d", "f", "e"]
print (alphabet)

alphabet.sort()
print (alphabet)

alphabet.sort(reverse=True)
print (alphabet)
#This program outputs:
#['c', 'b', 'a', 'd', 'f', 'e']
#['a', 'b', 'c', 'd', 'e', 'f']
#['f', 'e', 'd', 'c', 'b', 'a']
#Sort can be used for soring numbers and letters.

#Sort 03
friends = ["Shuvo", "Tuhin", "Tanvir", "Dipu", "Siyam"]
print (friends)

friends.sort()
print (friends)

friends.sort(reverse=True)
print (friends)
#This program outputs:
#['Shuvo', 'Tuhin', 'Tanvir', 'Dipu', 'Siyam']
#['Dipu', 'Shuvo', 'Siyam', 'Tanvir', 'Tuhin']
#['Tuhin', 'Tanvir', 'Siyam', 'Shuvo', 'Dipu']

#Clear 00
friends = ["Shuvo", "Tuhin", "Tanvir", "Dipu", "Siyam"]
friends.clear()
print (friends)
#This program outputs: []
#Clear method deletes the items of a list.
#Clear works like "del list_name [:]"

#Concatenation 00
numbers = [4,6,1,3,8,5,7,9,2]
alphabet = ['c', 'b', 'a', 'd', 'f', 'e']
c = numbers + alphabet
print (c)
#This program outputs: [4, 6, 1, 3, 8, 5, 7, 9, 2, 'c', 'b', 'a', 'd', 'f', 'e']

#File Operations 00
var = open("file.txt")
#content = var.read()
#print (var.read())
print (var.readline())
#for lines in var:
    #print (var.readline())

#This program outputs: lorem ipsum (Since lorem ipsum was written in the "file.txt" file in the same directory).
#It is required to open a file at first using open() command. Open must have one and only one argument.
#Open is a function so used WITHOUT dot notation.
#But there is no function named read.
#Read is used with dot notation and variable name.
#readline() method reads the first line of a file.

#File Operations 01
var = open("file.txt", "w")
var.write ("Testing")
var = open("file.txt")
print (var.read())
#content = var.read()
#print (var.read())
#print (var.readline())
#for lines in var:
    #print (var.readline())

#This program outputs: Testing
#Since lorem ipsum was replaced using
#"var = open("file.txt", "w")"
#"var.write ("Testing")"
#in the same directory.

#File Operations 02
doc = open ("file.txt")
print (doc.read())
doc.close()

edit = open ("file.txt", "w")
edit.write ("Hello Python")
edit.close()

ae = open ("file.txt")
print (ae.read())

#This program outputs as below:
#Hello Py
#Hello Python
#Here,the "w" must be in lowercase. Writing in uppercase shows error: "ValueError: invalid mode: 'W'"

#File Operations 02
t = "A quick brown fox jumps over the lazy dog."
q = 3.1416

be = open ("file.txt")
rbe = be.read()
print (rbe)

e = open ("file.txt", "w")
e.write (str(t))
e.write (" Pi = 3.1416")
#e.write (str(q))
e.close()

p = open("file.txt")
v = p.read()
print (v)

#To write non string type data it is required to convert that data into string using "str(that_data)" or use "".
#Otherwise, it shows: "TypeError: write() argument must be str, not float"

'''
Methods use dot notation with variable name:
index, append, extend, remove, sort, count, find, pop, replace, reverse, clear, upper, lower, capitalize, read, readline, write

Funtions go directly WITHOUT dot notation:
print, sum, len, round, min, max, type, del, open, sorted

A method looks like this: something.method()
And a function looks like this: function(something)
'''

#Function 00
def hello():
    print ("Hello world!")
#After running this, the program does not print anything.
#But, if "hello ()" is run in the console or included in the next line at third line it outputs "Hello world!"

#Function 01
def greet (name):
    print ("Welcome to Python programming", name)

greet("x")
greet("y")
#This program outputs as below:
#Welcome to Python programming x
#Welcome to Python programming y
#To get a data processed using a function, it is required to pass that data through the function using the parameter(s) in parentheses.

#Function 02
def add (a,b):
    return (a + b)

def sub (a,b):
    return (a - b)

def mul (a,b):
    return (a * b)

def div (a,b):
    return (a/b)

print (add (22,7))
print (sub (22,7))
print (mul (22,7))
print (div (22,7))

#This program outputs as below:
#29
#15
#154
#3.142857142857143

#Using functions it is easy to reuse the functions when necessary.

#Function 03
def max (a,b=0):
    if a > b:
        return ("a is bigger")
    if a < b:
        return ("a is smaller")
    if a == b:
        return ("a and b are equal")

print (max(6,7))
print (max(9)) #Since one parameter is given, it uses b=0 as the value of second parameter [as defined within the function].
print (max(6,6))

#This program outputs as below:
#a is smaller
#a is bigger
#a and b are equal

#Function 04
def nc (a):
    return bin(a), oct (a), hex (a)

print (nc(10))
#This program outputs: ('0b1010', '0o12', '0xa',)
#It is possible to use multiple returns in a single line.

#Function 05
def nc (a,b):
    return bin(a), bin(b), oct(a), oct(b), hex(a), hex(b)

print (nc(10,11))
#This program outputs: ('0b1010', '0b1011', '0o12', '0o13', '0xa', '0xb')
#Besides using multiple returns, it is also possible to use multiple parameters in a single line.

#Function 06
def nc (a,b,c):
    return bin(a), oct (a), hex (a), bin(b), oct (b), hex (b), bin(c), oct (c), hex (c)

print (nc(10,11,12))
#This program outputs: ('0b1010', '0o12', '0xa', '0b1011', '0o13', '0xb', '0b1100', '0o14', '0xc')
#It is possible to use multiple returns in a single line.

#Function 07
def b (a,b):
    return bin(a), bin(b)
x, y = (b(10,21))

print (x)
#This program outputs: 0b1010

#Function 08
def b (a,b):
    return bin(a), bin(b)
#x, y = (b(10,21))

print (b(10,21))
#This program outputs: ('0b1010', '0b10101')

#Function 09
def conv (n):
    print ("Binary:", bin(n))
    print ("Octal:", oct(n))
    print ("Helxadecimal:", hex(n))

x = int(input())

conv (x)

#Using 22 as input in the console this program outputs as below:
#Binary: 0b10110
#Octal: 0o26
#Helxadecimal: 0x16

#Function 10
def home (n="BD"):
    return print ("home country is:", n)
home ()
home ("US")
#It is posible to to set default value of a parameter.
#In such case, if NO value is given as parameter, the function processes the default value and outputs accordingly.
#Otherwise, it uses the given parameter.
#This program outputs:
#home country is: BD
#home country is: US

#Function 11
def max (x, y=14):
    if x > y:
        print (x, "is bigger")
    elif x < y:
        print (x, "is smaller")
    else:
        print ("both are equal")

#m = int (input ())
n = int (input ())
max (n)
#max (m,n)

#For three tests with 13, 14, 15 this program outputs:
#13 is smaller
#both are equal
#15 is bigger
#But if we use two parameter the usnig two inputs, the programs compares two inputs and outputs accordingly.

#Function 12
def binary(a, b):
    return bin(a), bin(b)
x, y = (binary(12, 14))
print(x)
print(y)
#This program outputs:
#0b1100
#0b1110
#It is possible to assign the converted value in two different variables and print just one.

#Function 13
def print_square (numbers):
    for item in numbers:
        print (item ** 2)

number_list = [2,3,4,5,6]
print_square(number_list)
#This program outputs:
#4
#9
#16
#25
#36
#It is possible to define functions and use it for iterable items like list too.

#Function 14
def exp (inputList, e):
    for items in inputList:
        print (items ** e)

il = [2, 4, 43, 67, 38]
ex = int (input())

exp (il, ex)

#When giving 2 as input for the value of ex, this program outputs:
#4
#16
#1849
#4489
#1444
#It is possible to define functions and use it for iterable items like list too.

#Function 15
def exp (inputList, e, exponentedList):
    #InputList is for the input list, e is for exponent input from user, exponentedList is for storing Exponented List after operation.
    for items in inputList:
        ed = (items ** e)
        #ed variable is for storing exponented value and printing it afterwards as well as appending the value to a new list.
        print (ed)
        exponentedList.append (ed)
        #For appending the value to a new list.
        print (exponentedList)
        #For printing the new list where the exponented values were appended.

il = [2, 4, 43, 67, 38] #Using il in the place of inputList (first parameter)
ex = int (input()) #Using ex in the place of e (second parameter)
eil = [] #Using eil in the place of exponentedList (third parameter)

exp (il, ex, eil) #Using the function 'exp' that was defined earlier.

#When giving 2 as input for the value of ex, this program outputs:
#4
#[4]
#16
#[4, 16]
#1849
#[4, 16, 1849]
#4489
#[4, 16, 1849, 4489]
#1444
#[4, 16, 1849, 4489, 1444]
#It is possible to use functions and put the outputs in a list too.

#Tuple 00
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (num)
num[-1] = -9
print (num)

tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print (tpl)
num[-1] = -9
print (tpl)
#This program outputs as below:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, -9]
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#TypeError: 'tuple' object does not support item assignment
#Tuple is IMMUTABLE.
#List is MUTABLE.
#Tuple can be used in places where the items are NOT required to be mofified.

#Dictionary 00
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14}
print (friends["Shuvo"])
#This program outputs: 15

#Dictionary 01
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
print (friends["Shuvo"])
#This program outputs: 20
#Using a key for more than one time updates the value of that key.

#Dictionary 02
friends = {'Shuvo': 15, 'Tuhin': 13, 'Tanvir': 14, 'Dipu': 13, 'Siyam': 14}
print (friends)
#This program outputs: {'Shuvo': 15, 'Tuhin': 13, 'Tanvir': 14, 'Dipu': 13, 'Siyam': 14}

#Dictionary 03
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
print (friends.keys())
#This program outputs: dict_keys(['Shuvo', 'Tuhin', 'Tanvir', 'Dipu', 'Siyam'])
#Note that, the keys exclude duplicates.

#Dictionary 04
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
print (friends.values())
#This program outputs: dict_values([20, 13, 14, 13, 14])
#Note that, like the keys, values also exclude duplicates.
#But, dictionary keeps the first key and the last value for that key.

#Dictionary 05
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
print (friends.items())
#This program outputs: dict_items([('Shuvo', 20), ('Tuhin', 13), ('Tanvir', 14), ('Dipu', 13), ('Siyam', 14)])

#Dictionary 06
friends = dict(Shuvo = 15, Tuhin = 13, Tanvir = 14, Dipu = 13, Siyam = 14)
print (friends)
#This program outputs: {'Shuvo': 15, 'Tuhin': 13, 'Tanvir': 14, 'Dipu': 13, 'Siyam': 14}
#It is possible to easily convert a string to a dictionary.
#This also works with same output: print (dict(Shuvo = 15, Tuhin = 13, Tanvir = 14, Dipu = 13, Siyam = 14))
#However, if feeling curious, it is NOT possible to make a list like the above way.
#Trying "print (list(Shuvo = 15, Tuhin = 13, Tanvir = 14, Dipu = 13, Siyam = 14))" shows "TypeError: list() takes no keyword arguments"

#Dictionary 07
print (type({'Shuvo': 15, 'Tuhin': 13, 'Tanvir': 14, 'Dipu': 13, 'Siyam': 14}))
#This program outputs: <class 'dict'>

#Dictionary 08
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
print (list (friends))
#This program outputs: ['Shuvo', 'Tuhin', 'Tanvir', 'Dipu', 'Siyam']
#It is possible to make a list of keys of a dictionary using list function.

#Dictionary 09
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
for i in friends:
    print (friends[i])
#This program outputs as below:
#20
#13
#14
#13
#14

#Dictionary 10 
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
for key in friends:
    print ("Age of ", key, "is ", friends[key])
#This program outputs as below:
#Age of  Shuvo is  20
#Age of  Tuhin is  13
#Age of  Tanvir is  14
#Age of  Dipu is  13
#Age of  Siyam is  14

#Dictionary 11
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
for k,v in friends.items():
    print ("Age of ", k, "is ", v)
#This program outputs as below:
#Age of  Shuvo is  20
#Age of  Tuhin is  13
#Age of  Tanvir is  14
#Age of  Dipu is  13
#Age of  Siyam is  14

#Dictionary 12
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
friends["Siyam"] = 12
print (friends)
#This program outputs: {'Shuvo': 20, 'Tuhin': 13, 'Tanvir': 14, 'Dipu': 13, 'Siyam': 12}

#Dictionary 13
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
friends["Sife"] = 21
print (friends)
#This program outputs: {'Shuvo': 20, 'Tuhin': 13, 'Tanvir': 14, 'Dipu': 13, 'Siyam': 14, 'Sife': 21}

#Dictionary 14
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
del friends ["Shuvo"]
print (friends)
#This program outputs: {'Tuhin': 13, 'Tanvir': 14, 'Dipu': 13, 'Siyam': 14}

#Dictionary 15
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
friends.clear()
print (friends)
#This program outputs: {}

#Dictionary 16
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
del friends
print (friends)
#This program outputs: NameError: name 'friends' is not defined

#Dictionary 17
friends = {"Shuvo":15, "Tuhin":13, "Tanvir":14, "Dipu":13, "Siyam":14, "Shuvo":20}
print (len (friends))
#This program outputs: 5
#Note that, like before, it disregards duplicates.

#Set 00
book_set = {"Bangla", "English", "Math", "Physics", "Math"}
print(book_set)
#Set uses braces.
#Sets removes duplicates
#Printing a set changes the order of the items every time.

#Set 01
print (len (book_set))
#This program outputs: 4

#Set 02
rs = {"Bangla", 3.1416, True}
rs.add ("English")
print (rs)
#This program outputs: {True, 'Bangla', 'English', 3.1416}

#Set 03
rs = {True, "Bangla", "English", 3.1416}
rs.remove(3.1416)
rs.remove(True)
rs.remove("Bangla")
print (rs)
#This program outputs: {'English'}

#Set 04
rs = {True, "Bangla", "English", 3.1416}
for i in rs:
    print (i)
#This program outputs as below:
#Bangla
#True
#3.1416
#English
#It is possible to use loops in set.
#Remember, printing a set changes the order of the items every time.

#Set 05
rs = {True, "Bangla", "English", 3.1416}
p = rs.pop()
print (p)
print (rs)
#Although pop method can be used with a set, BUT, it raises problem since set items does NOT follow specific order.
#However, it can be used in a lottery basis.
#Output varies!

#String 00
a = 10
b = 50
print ("value of a = {}, value of b = {}" .format(a, b))
#This program outputs: value of a = 10, value of b = 50
#To format a string, use {} and .format(variable_names) at last.

#String 01
a = 10
b = 50
c = "value of a = {}, value of b = {}" .format(a, b)
print (c)
#This program outputs: value of a = 10, value of b = 50
#It is possible to use another variable for string formation too.

#String 02
a = 10
b = 50
c = "value of a = {}, value of b = {}"
print (c .format(a, b))
#This program outputs: value of a = 10, value of b = 50
#This also works.

#String 03
a = 10
b = 50
c = "value of a = {}, value of b = {}"
print (c .format(b, a)) #Check this line's difference
#This program outputs: value of a = 50, value of b = 10
#Here the value of b is printed at first.

#String 04
name  = "Guido van Rossum"
print ("Developer name of Python programming is {}!" .format(name))
#This program outputs: Developer name of Python programming is Guido van Rossum!

#String 05
my_list = [ 1, 2, 3, 4]
print ("my list {} " .format(my_list))
#This program outputs: my list [1, 2, 3, 4]

#String 06
s = "This is a string."
print(s.split())
#This program outputs: ['This', 'is', 'a', 'string.']

#String 07
s = "This is a string."
k = s.split()
for i in k:
     print (i)
#This program outputs as below:
#This
#is
#a
#string.

#String 08
s = "This is a string."
words = s.split()
for w in words:
    print (w)
print (" " .join(words)) #Check this line
#This program outputs as below:
#This
#is
#a
#string.
#This is a string.

#String 09
s = "This is a string."
words = s.split()
for w in words:
    print (w)
print ("-".join(words)) #Check this line's difference
#This program outputs as below:
#This
#is
#a
#string.
#This-is-a-string.

#String 10
s = "This is a string."
words = s.split()
for w in words:
    print (w)
print ("".join(words)) #Check this line's difference
#This program outputs as below:
#This
#is
#a
#string.
#Thisisastring.

#String 11
s = "This is a string."
words = s.split()
for w in words:
    print (w)
print (.join(words)) #Check this line's difference
#This program outputs: SyntaxError: invalid syntax

#String 12
s = ["This", "is", "a", "string."]
print (" " .join(s))
#This program outputs: This is a string.

#String 13
s = "This is a String!"
print (s)
print (s.lower())
print (s.upper())
print (s.capitalize())
print (s.title())
print (s.swapcase())
#This program outputs as below:
#This is a String!
#this is a string!
#THIS IS A STRING!
#This is a string!
#This Is A String!
#tHIS IS A sTRING!

#String 14
s = "This is a String!"
#k = s.replace("This","That")
#print(k)
print (s.replace("This","That"))
#This program outputs: That is a String!
s.replace("This","That")
print(s)
#This program outputs: This is a String!

#Replace requires using another variable to hold the new data.
#It does NOT directly modifies the variable.

#String 15
stri = "This is a string!"
print (stri.count("s"))
k = stri.count("s")
print (k)
#This program outputs as below:
#3
#3
#Two ways work fine.

#String 16
stri = "This is a string!"
print (stri.find("i"))
k = stri.find("i")
print (k)
#This program outputs as below:
#2
#2
#Two ways work fine.

#String 17
stri = "This is a string!"
print (len(stri))
k = len (stri)
print (k)
#This program outputs as below:
#17
#17
#Two ways work fine.

#Random 00
import random

print (random.random())
#This program generates a random number betwen 0 and 1.
print (random.randrange(4,40))
#This program (using random.randrange) generates a random number betwen two given limits. [Here, 4 and 40].
#Outputs varies.

#RegEx 00
k = open ("lm.txt")
import re

for line in k:
    if re.search ("(waken|open)ed", line):
        print (line)
k.close()
#This program outputs: This soon wakened the Lion, who placed his huge paw upon him and opened his big jaws to swallow him.

#RegEx 01
k = open ("lm.txt")
import re

for line in k:
    match = re.search ("(waken|happen)ed", line)
    if match :
        print (match.group())
k.close()
#This program outputs as below:
#wakened
#happened

#RegEx 02
k = open ("lm.txt")
import re

for line in k:
    print (re.sub ("Lion", "Tiger", line))
k.close()
#This program replaces all Lion with Tiger and outputs accordingly.

