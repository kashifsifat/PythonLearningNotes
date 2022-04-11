n = int(input("Lower: "))
ut = int(input("Upper: "))
ui = ut + 1
sum = 0

print ("\nPrime number(s) between the given range is/are as follows:")

if n < 2:
    n = 2

for i in range (n,ui):
    isp = True
    
    for j in range (2,i):
        if i%j == 0:
            isp = False

    if isp:
        print (i)
        sum += i

print ("\nSum =", sum)