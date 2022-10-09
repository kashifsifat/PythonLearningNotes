print ("How many tables do you want?\n")

tab_req = int (input("Table required: "))

ask = 0

tables_of = []

while ask < tab_req:
    t = int (input("Table of: "))
    tables_of.append (t)
    ask += 1

index = 0

#print (" ")

for j in tables_of:
        print ("\nHere is the", str(tables_of[index]) + "'s table:")
        index += 1

        for i in range (0,11):
            print (str(i), "x", str(j), "=", i * j)

        #index += 1
