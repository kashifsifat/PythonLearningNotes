n = int (input ("Persons: "))

if n >= 1:
    m = n - 1
    hs = ((m + 1) / 2) * m
    print ("Handshakes:", hs)
    
else:
    print ("Invalid Input!")
    
# Alternative implementation:
print ((n ** 2 - n) / 2)