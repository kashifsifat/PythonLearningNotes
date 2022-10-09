n = int (input ("Table of: "))

print ("\nHere is the", str (n) + "'s table:")

for i in range (0,11):
    print (str (i), "x", str (n), "=", n * i)
