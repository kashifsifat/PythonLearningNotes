s = int (input("Lower Limit: "))
e = int(input("Upper Limit: "))

if s < 2:
    s = 2

for n in range (s, e):
        is_Prime = True
        
        for i in range (2, n):
                if n % i == 0:
                    is_Prime = False
                    break
            
        if is_Prime:
            print (n)