#Basic Calculation Program 00

sum = 0
avg = 0
count = 1
lons = []
while count > 0:
    i = float(input("Number " + str(count) + ": "))
    sum += i
    avg = sum / count
    lons.append (i)
    print ("List of inputs (Unordered):", lons)
    print ("Sum:", sum)
    print ("Average: ", avg)
    print ("Min:", min(lons))
    print ("Max:", max(lons))
    print ("Count:", count)
    lons.sort()
    print ("List of inputs (Sorted: Ascending):", lons)
    lons.sort(reverse=True)
    print ("List of inputs (Sorted: Descending):", lons)
    print (" ")
    count += 1
