q = int(input("Enter a number to check its primality: "))
is_Prime = True

if q < 2:
    is_Prime = False
    
for i in range (2,q):
    if q % i == 0:
        is_Prime = False

if is_Prime == True:
    print (q, "is a prime number")
    
if is_Prime == False:
    print (q, "is not a prime number")