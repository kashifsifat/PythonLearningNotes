'''
This program can be used for getting the answer to the question like:
Which number(s) are dividable with x from y to z.
'''
x = int (input ("From: "))
y = int (input ("Upto: "))
z = int (input ("What?: "))

s = []
c = 0
for i in range (x,(y+1)):
    if i % z == 0:
        #print (i)
        s.append (i)
        c += 1

print ("\nTotal numbers divisible with", z, "from", x, "to", y, "(inclusive) is/are:", c, "\n")

print ("Numbers:", s)