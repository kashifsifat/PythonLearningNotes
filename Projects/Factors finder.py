x = int (input("Number: "))
c = 0
print ("Factor(s):")

for i in range (1,(x+1)):
    if x % i == 0:
        print (i)
        c += 1
        
print ("Total factors:", c)