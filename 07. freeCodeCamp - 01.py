#Print 00
print ("Si\nFu")
#This program outputs as below:
#Si
#Fu

#Case Checking 00
a = "sifat kashif"
print (a.isupper())
print (a.islower())
#This program outputs as below:
#False
#True

#Basic Calculations 00
a = -5
print (abs(a))
#This program outputs: 5

print (pow(2,10))
#This program outputs: 1024

print (round(2.6))
#This program outputs: 1024

import math
print (math.floor(2.6))

from math import *
print (floor(2.6))
#Both of the above programs output: 2
#But, when using "import math", it is required to use math.function_name.
#OTOH, while using "from math import *" it is NOT required to use math.function_name. Instead, directly using the function_name is possible.

#Insert 00
c = ["j", "t", "s0", "s1", "s2"]
a = ["s3"]
c.insert (5, "s3") #insert (index, item)
print (c)
#This program outputs: ['j', 't', 's0', 's1', 's2', 's3']

#Copy 00
c = ["z", "j", "t", "s0", "s1", "s2", "s2"]
#k = list(c)
k = c.copy()
k[-1] = "z"
print (c)
#This program outputs: ['z', 'j', 't', 's0', 's1', 's2', 's2'] (NOT modifying the value of c)
#It is possible to use k = list(c) to achieve this too
#But, if used directy as k = c, the program outputs ['z', 'j', 't', 's0', 's1', 's2', 'z'] (Modifying the value of c)

#Function 00
def cube (n):
    return (n * n * n)

r = cube (2)
print (r)
print (type(2.0))
#This program outputs as below:
#8
#<class 'float'>

#Function 01
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    if num3 >= num1 and num3 >= num2:
        return num3

print (max_num(3,4,5))
#This program outputs: 5

#Function 02
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(3,4,5))
#This program outputs: 5

#Function 03
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "*":
    print (num1 * num2)
elif op == "/":
    print (num1 / num2)
else:
    print ("Invalid operator")

#Dictionary 00
monthConversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "April":"Apr",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
    }
x = input()
y = x.capitalize()

print (monthConversion.get(y))
print (monthConversion[y])
#Using get method is useful for situations where there is chance for any key not found in dictionary.
#In such case, directly accessing the key using [] shows error, but using get method shows 'None' instead of an error.
#However, it is also possible to assign a default value to show in case of an error. Like below:
print (monthConversion.get(y, "Not found"))

#Guessing Game 00
secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input ("Enter guess: ")
    
print ("You win!")

#Guessing Game 01
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input ("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("Out of Guesses, you lose!")
else:
    print ("You win!")

#Alternative implementation below:
#if guess == secret_word:
#    print ("You won!")
#else:
#    print ("You lost!")

#For Loop 00
for i in range (5):
    if i == 0:
        print ("First iteration")
    else:
        print ("Not first")
#This program outputs as below:
#First iteration
#Not first
#Not first
#Not first
#Not first

#Exponent Calculator Function 00
b = int (input ())
e = int (input ())

def exponent (base, exp):
    result = 1
    for i in range (exp):
        result = result * base
    return result

print (exponent(b,e))

#2D List 00
num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
    ]

print (num_grid[2][1])
#This program outputs: 8

#2D List 01
num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
    ]

print (num_grid)
#This program outputs: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for i in num_grid:
    for n in i:
        print (n)
#This program outputs as below:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#0

for i in num_grid:
    print (i)
#This program outputs as below:
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]
#[0]

#Language Translator 00
s = input()
sl = s.lower()
v = ["a", "e", "i", "o", "u"]
so = ""

for i in sl:
    if i in v:
        so += "g"
    if i not in v:
        so += i

print (so)

#Language Translator 01
def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
        #Alternatively,
        #if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print (translate(input("Enter a phrase: ")))
#This program outputs as below:
#Enter a phrase:
#Then after giving "to be or not to be" as an input,
#This program outputs:
#tg bg gr ngt tg bg

#Language Translator 02
def translate (phrase):
    translation = ""
    for letter in phrase:
        #if letter in "AEIOUaeiou":
        #Alternatively,
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print (translate(input("Enter a phrase: ")))
#This program outputs as below:
#Enter a phrase:
#Then after giving "To be or not to be" as an input,
#This program outputs:
#Tg bg gr ngt tg bg

#Try & Except 00
try:
    #value = 10 / 0
    number = int (input("Enter a number: "))
    print (number)
except ZeroDivisionError:
    print ("Divided with zero")
except ValueError:
    print ("Invalid input")

print ("Program is still runing")

#File Operation 00
j = open ("tt.txt", "a") #Using "a" for appending the next line at the end of the file.
j.write ("test")
j.close ()

rn = open ("tt.txt")
print (rn.read ())
rn.close ()
#Use "r" for read, "w" for write, "a" for append, "r+" for read and write.

#File Operation 01
j = open ("tt.txt", "r+")
k = j.readlines()
for i in k:
    print (i)
#Note the words 'readline' and 'readlines'. Those are different and behave differently.

#File Operation 02
j = open ("tt.txt", "r+")
k = j.readlines()
print (k)
#This program outputs the lines in a list.
