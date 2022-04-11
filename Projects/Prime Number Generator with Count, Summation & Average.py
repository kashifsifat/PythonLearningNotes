Lt = int (input ("Lower Limit: "))
Ut = int (input ("Upper Limit: "))
print ("")
U = Ut + 1 #To make upper limit inclusive
C = 0 #C for counting how many prime numbers are in the range
S = 0 #S for sum of the prime numbers in the range
A = 0 #A for average of the prime numbers in the range

print ("Prime number(s) from", Lt, "to", Ut, "(inclusive) is/are: ")

if Lt <= 2:
    L = 2
else:
    L = Lt

for i in range (L, U):
    isp = True
    
    for j in range (2, i):
        if i % j == 0:
            isp = False
            
    if isp:
        print (i)
        S += i
        C += 1

A = S / C

print ("")

#print ("There is/are", C, "prime number(s) from", Lt, "to", Ut, ".")
#print ("Sum of the", C, "prime number(s) is:",  S, ".")
#print ("Average of the", C, "prime number(s) is:",  A, ".")
#print ("")

#Simplified Implemetation

print ("Count:", C)
print ("Sum:", S)
print ("Average:", A)
