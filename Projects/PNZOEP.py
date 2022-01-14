#CF 00 (Odd-Even-Prime)

i = int (input ())

is_positive = False
is_neutral = False
is_even = False
is_prime = True

if i > 0:
    is_positive = True
elif i < 0:
    is_positive = False
elif i == 0:
    is_neutral = True

if i % 2 == 0:
    is_even = True

if i == 1:
    is_prime = False

if i > 2:
    for n in range (2,i):
        if i % n == 0:
            is_prime = False

if ((is_positive == True) and (is_even == True) and (is_prime == True) and (is_neutral == False)):
    print (i, "is a positive even prime number.")
    
elif ((is_positive == True) and (is_even == True) and (is_prime == False) and (is_neutral == False)):
    print (i, "is a positive even non-prime number.")
    
elif ((is_positive == True) and (is_even == False) and (is_prime == True) and (is_neutral == False)):
    print (i, "is a positive odd prime number.")
    
elif ((is_positive == True) and (is_even == False) and (is_prime == False) and (is_neutral == False)):
    print (i, "is a positive odd non-prime number.")
    
elif ((is_positive == False) and (is_even == True) and (is_neutral == False)):
    print (i, "is a negative even number.")
    
elif ((is_positive == False) and (is_even == False) and (is_neutral == False)):
    print (i, "is a negative odd number.")
    
elif (is_neutral == True):
    print (i, "is zero. And zero is a non-negative, non-positive, non-prime, even number. (Since, even number = 2n. And, 2 x 0 = 0).")