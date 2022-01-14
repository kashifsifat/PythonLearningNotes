#Calculating Sum of All Digits 00
sum = 0

n = int (input ("Number: "))
k = str (n)

for i in k:
    #print (i)
    sum += int (i)

print ("Sum of all digits in the number:", sum)