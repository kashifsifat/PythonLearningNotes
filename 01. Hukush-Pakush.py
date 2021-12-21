#Print
print ("Bismillah!")

#Variable 00
base = 232.5
height = 1200
area = 0.5 * base * height
print(area)

#Variable 01
base = float(input("Base: "))
height = float(input("Height: "))
area = 0.5 * base * height
print(area)

#List
cart = ["potato", "rice", "onion", "lemon", "oil", "egg", "banana"]
print (cart[0], cart[2], cart[3], cart[5])

#Dictionary
gradschool = {
    "azhar":"nu_fin",
    "alu":"du_fin",
    "ashik":"sust_math",
    "tanay":"nstu_ict",
    "sifu":"nu_mkt"
}
print(gradschool[input("name: ")])

#CF
Monthly_Income = int(input("Monthly Income = "))

if Monthly_Income < 10000:
    print ("How dare!?")
elif Monthly_Income <= 20000:
    print ("Find a better job")
elif Monthly_Income > 20000:
    print ("Potential bride")

#CFwithBoolean 00
today = "monday"
sifat = 1000
ashik = 399

if today == "monday" and sifat > 300 and ashik > 300:
    print ("Going to cinema!")
else:
    print ("not today")

#CFwithBoolean 01
today = "monday"
money = 1000

if today == "monday" and money > 300:
    print ("Going to cinema!")
else:
    print ("not today")

#CFwithBoolean 02
Monthly_Income = int(input("Monthly Income: "))
Age = int(input("Age: "))

if Monthly_Income >= 20000 and Age >= 18:
    print ("Get Married!")
else:
    print ("Be patient")

#CFwithBoolean 03
Monthly_Income = int(input("Monthly Income: "))
Age = int(input("Age: "))

if Monthly_Income >= 20000 and Age >= 18:
    print ("Get Married!")
elif Age < 18 and Monthly_Income < 20000:
    print ("How dare!")
elif Monthly_Income < 20000:
    print ("Look for a better job!")
elif Age < 18:
    print ("You might be sued!")

#Loop 00
#WhileLoop
i = 0
while i < 10:
    print ("learning loop")
    i = i + 1
#Heads up! Do not forget to use the i = i + 1 incrementer when using while loop. Rather, it becomes a continous loop!!!

#Loop 01
#ForLoop
for i in range (10):
    print ("hi")

#Note that:
#In "While loop" we need to assign a primary value for the variable. But, in the case of "For loop" we do not need to do that.
#In "While loop" we need to use the i = i + 1 for incrementing the value of i. But, when we use "for loop" we do not need to use that.

#Loop 02
#ForLoop
for i in range (6, 10):    
    print (i * i)
#Note that:
#The case of Range is inclusive for the lower limit but exclusive for the upper limit.
#So, here the program outputs the values of six squared to the nine squared - but not ten squared.
    
#Loop 03
#WhileLoop
#Odd numbers upto 10 using While loop
i = 1
while i < 10:
    print (i)
    i = i + 2

#Loop 04
#ForLoop
#Odd numbers upto 10 using For loop
for i in range (1, 10, 2):
#Here in the parenthesis (lower_limit, upper_limit, increment).
#If there is no lower_limit, upper_limit, increment For loop start from the first item or 0.
#As mentioned earlier, Range is inclusive for the lower limit but exclusive for the upper limit.
    print (i)

#Loop 05 (All in a nutshell)
#Odd 1-10 using While
print ("WL_o")
i = 1
while i < 10:
    print (i)
    i = i + 2
#Odd 1-10 using For
print ("FL_o")
for i in range (1,10,2):
    print (i)
#Even 1-10 using While
print ("WL_e")
i = 0
while i < 10:
    print (i)
    i = i + 2
#Even 1-10 using For
print ("FL_e")
for i in range (0,10,2):
    print (i)
#When using loop, if we put the print command in the loop (with same indent), program outputs all the numbers in that loop's sequence.
#On the contrary, if we put the print command outside the loop, program outputs only the last number in that loop's sequence.

#Loop 06
#Loop In A List (For Loop)
fruits = ["apple", "orange", "banana", "mango", "cherry"]
for i in range (5):
    print (fruits[i])
#If there is no lower_limit, upper_limit, increment, For loop start from the first item or 0.

#Loop 07
#Loop In A List (While Loop)
fruits = ["apple", "orange", "banana", "mango", "cherry"]
i = 0
while i < 5:
    print (fruits[i])
    i = i + 1

#In looped list, using "print (fruits)" instead of "print (fruits[i])" outputs the whole list five times instead of printing the list items.

#Loop 08
#Loop In A List (Python Style)
fruits = ["apple", "orange", "banana", "mango", "cherry"]
for i in fruits:
    print (i)
#However, you can use any letter/words instead of 'i' here. For example,
    #for fruit in fruits:
    #print (fruit)
        #Is okey here too.

#Break 00
fruits = ["apple", "orange", "banana", "jambura", "mango", "cherry"]
found = "no"
for fruit in fruits: #for "anything"/"whatever" in "list name":
    if fruit == "jambura": #if "anything/whatever (must be same as before)" == "querry":
        found = "yes"
        break
if found == "yes":
    print("we have jambura!")
else:
    print("sorry!")
    
#Break 01
fruits = ["apple", "orange", "banana", "mango", "cherry"]
if "jambura" in fruits:
    print("we have jambura")
if "jambura" not in fruits:
    print("sorry!")

#Break 02
fruits = ["apple", "orange", "banana", "mango", "cherry"]
if "jambura" in fruits:
    print("we have jambura")
else:
    print("sorry!")

#Continue 00

sum = 0
for i in range(1, 100):
    if i % 2 == 0:
        continue
    sum = sum + i

print(sum)

#The above program outputs the sum of all odd numbers from 0 to 100
#Note that, it requires to add the 'continue' BEFORE the line when we calculate the sum.
#Actualy here the 'continue' is in BETWEEN 'if' and 'sum'.

#However, I could find another way to achive the same goal without using 'continue'. That code is mentioned below:

sum = 0
for i in range (1,100,2):
    sum = sum + i
    
print (sum)

#Printing the summation of all odd numbers from 001 to 100 (Three methods)

print ("Using 'For'")
sum = 0
for i in range (1,100,2):
    print (i)
    sum = sum + i
print (sum)

print ("Using 'While'")
i = 1
sum = 0
while i < 100:
    print (i)
    sum = sum + i
    i = i + 2
print (sum)

print ("Using 'For' and 'Continue'")
sum = 0
for i in range (1,100):
    if i % 2 == 0:
        print (i + 1)
        #sum = sum + i
        continue
    sum = sum + i
print (sum)

#Function 00
def square(x):
    return x * x

print(square(9))

#When using 'def' do NOT forget to add ':' at last and 'return' in the following line.

#Function 01
n = int(input("Number: "))
e = int(input("Exponent: "))

def exponent (n):
    return n ** e

print (exponent(n))

#The program can be used to calculate the exponent value of any given number.

#Function 02
n = int(input("Number: "))

def factorial (n):
    if n == 1:
        return n
    else:
        return n * factorial (n - 1)

print (factorial(n))

#The program can be used to calculate the factorial of any given number.

#Function 03
for x in range(2, 101):
    is_prime = True

    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print(x)

#The program can be used for printing all prime numbers from 002 to 100.
        
#Function 04
u = int(input("Prime Numbers Upto: "))

for x in range (2,u):
    is_Prime = True
    
    for n in range (2,x):
        if x % n == 0:
            is_Prime = False
            break
    
    if is_Prime == True:
        print (x)

#The program can be used for printing all prime numbers from 002 to any given number.
        
#Function 05
l = int(input("Prime Numbers From: "))
u = int(input("Prime Numbers Upto: "))

for x in range (l,u):
    is_Prime = True
    
    for n in range (2,x):
        if x % n == 0:
            is_Prime = False
            break
    
    if is_Prime == True:
        print (x)

#The program can be used for printing all prime numbers from any given number to any given number.
#But, here the problem is, if the user inputs 0 or 1 in the from field, the program outputs 0 and 1 as prime too.
#Let's correct that glitch. [See, #Function 06].
        
#Function 06
l = int(input("Prime Numbers From: "))
u = int(input("Prime Numbers Upto: "))

for x in range (l,u):
    is_Prime = True
    if x < 2:
        is_Prime = False
    
    for n in range (2,x):
        if x % n == 0:
            is_Prime = False
            break
    
    if is_Prime == True:
        print (x)

#The program can be used for printing all prime numbers from any given number to any given number.
#Besides, this program can disregard 0 and 1 if the user inputs 0 or 1 in the from field.
#So, this program corrects the glitch of its previous version [See, #Function 05].

#For testing purpose the list of prime numbers are given below:
# From 00 to 10: 2 3 5 7
# From 10 to 20: 11 13 17 19
# From 20 to 30: 23 29
# From 30 to 40: 31 37
# From 40 to 50: 41 43 47
# From 50 to 60: 53 59
# From 60 to 70: 61 67
# From 70 to 80: 71 73 79
# From 80 to 90: 83 89
# From 90 to 100: 97

#Concatenate 00

name = input()

print ("You have a beautiful name"+" "+name)

print ("You have a beautiful name",name)

#When using "+" for concatenate, it is required to add " " (space) for space.
#But, when using "," for concatenate, it is NOT required to add " " (space) for space.

#OOP 00
class Calculator:

    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

c = Calculator()
c.set(2, 2)

print(c.add())

#OOP 01
class Calculator:

    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

first = Calculator()
second = Calculator()

first.set(2, 2)
second.set(5, 12)

print(first.add())
print(second.add())

#OOP 02
class Calculator:

    def set(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


class NewCalculator(Calculator):

    def multiply(self):
        return self.a * self.b

c = NewCalculator()
c.set(2, 3)
print(c.multiply())

#OOP 03
class Pet:

    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class Cat(Pet):

    def talk(self):
        print(self.name + ": meow!")


class Dog(Pet):

    def talk(self):
        print(self.name + ": hoof! hoof!")


class Tiger(Pet):

    def talk(self):
        print(self.name + ": halum!")


class Mouse(Pet):

    def talk(self):
        print(self.name + ": kich! kich!")


cat = Cat("bilai")
dog = Dog("kuttush")
tiger = Tiger("bug")
mouse = Mouse("idur")

cat.talk()
dog.talk()
tiger.talk()
mouse.talk()

#The above program outputs the follwing lines:
#bilai: meow!
#kuttush: hoof! hoof!
#bug: halum!
#idur: kich! kich!

#OOP 04
p = float (input())
q = float (input())

class Calculator:
    
    def set(self,a,b):
        self.a = a
        self.b = b
        
    def add (self):
        return self.a + self.b
    
    def sub (self):
        return self.a - self.b
    
    def mul (self):
        return self.a * self.b
    
    def div (self):
        return self.a / self.b
    
c = Calculator()
c.set (p, q)

print (c.add())

#Modules 00
import math

print(math.factorial(5))

