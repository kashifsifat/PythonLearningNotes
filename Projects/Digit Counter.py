#Digit Counter 00

#This program is for counting how many times a digit appears in a given range.

f = int (input ("From (inclusive): "))
cr = int (input ("To (inclusive): "))
cov = str (input ("Count what?: "))
cf = cr + 1
#Used f for floor, cr for ceiling raw, cov for counting value, cf for ceiling final

s = []
for i in range (f, cf):
    k = str (i)
    s.append (k)
    
#print (s)
#Used for checking whether the given range is generating a list properly.

svl = []
for i in s:
    for m in i:
        #print (m)
        #Used for checking whether the characters are splitting properly.
        svl.append (m)

#print (svl)
#Used for checking whether the splitted characters are getting added to a set properly.

print (svl.count (cov))
#Printing the final result.
