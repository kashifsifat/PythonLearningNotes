def gc ():
    given_list = []
    a_sort_list = []
    d_sort_list = []
    total = 0
    count = 1
    average = 0
    maximum = 0
    minimum = 0
    i = 1
    while i > 0:
        inp = float(input("Input_" + str(count) + ": "))
        given_list.append (inp)
        a_sort_list.append (inp)
        d_sort_list.append (inp)
        a_sort_list.sort()
        d_sort_list.sort(reverse=True)
        total += inp
        average = (total / count)
        maximum = max (given_list)
        minimum = min (given_list)
        print ("Items: ", given_list)
        print ("Sum: ", total)
        print ("Average: ", average)
        print ("Minimum: ", minimum)
        print ("Maximum: ", maximum)
        print ("Count: ", count)
        print ("Sorted (Ascending): ", a_sort_list)
        print ("Sorted (Descending): ", d_sort_list)
        count += 1
        print (" ")
        
gc()