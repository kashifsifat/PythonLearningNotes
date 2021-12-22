def exp (il, el, ol, e, ni=1, c=1):
    il = []
    ol = []
    el = []
    while c > 0:
        i = float (input("Input: "))
        il.append(i)
        e = float (input("Exponent: "))
        el.append(e)
        ol.append(i ** e)
        print ("List of Inputs: ", il)
        print ("List of Exponents: ", el)
        print ("List of Outputs: ", ol)
        print (" ")

li = []
le = []
lo = []
exp (li, le, lo, e=0)
