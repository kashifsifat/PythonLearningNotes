# Formula: C/5 = (F-32)/9 = (K-273.15)/5

cr = 1
while cr > 0:

    v = float (input ("Input Value: ")) # v stands for input value
    cf_temp = str (input ("Convert From (C/F/K): ")) # cf_temp stands for convert from temporary
    ct_temp = str (input ("Convert To (C/F/K): ")) # ct_temp stands for convert to temporary

    # Making the input case insensitive
    cf = cf_temp.upper()
    ct = ct_temp.upper()

    # From below, r_temp and r stand for temporary result and final result respectively
    # Using temporary result to add the degree sign in final result where needed


    # C-F
    if cf == "C" and ct == "F":
        r_temp = round ((9*v/5)+32, 3)
        r = str (r_temp)+"°"

    # C-K
    if cf == "C" and ct == "K":
        r = round ((v+273.15), 3)


    # F-C
    if cf == "F" and ct == "C":
        r_temp = round ((v-32)*5/9, 3)
        r = str (r_temp)+"°"

    # F-K
    if cf == "F" and ct == "K":
        r = round (((v-32)*5/9)+273.15, 3)


    # K-C
    if cf == "K" and ct == "C":
        r_temp = round (v-273.15, 3)
        r = str (r_temp)+"°"

    # K-F
    if cf == "K" and ct == "F":
        r_temp = round (((v-273.15)*9/5)+32, 3)
        r = str (r_temp)+"°"


    # Below portion is to return the input as output if both of the units are same
    if cf == ct:
        r = v

    print (r)
    print (" ")
