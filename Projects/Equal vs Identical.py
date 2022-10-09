a = [1,2]
b = [1,2]
#a=1
#b=1
print (id(a))
print (id(b))
print (a==b)
print (a is b)
#This program outputs as below:
#56895248
#14854424
#True
#False
#NB: IDs are different.

print(" ")

#a = [1,2]
#b = [1,2]
a=1
b=1
print (id(a))
print (id(b))
print (a==b)
print (a is b)
#This program outputs as below:
#1906698752
#1906698752
#True
#True
#NB: IDs are same.
