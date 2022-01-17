class Cal:


    def add (a,b):
        return (a + b)
  
    def sub (a,b):
        return (a - b)
  
    def mul (a, b):
        return (a *b)

    def div (a, b):
        return (a / b)

    def exp (a,b):
        return (a ** b)
  
    def mod (a,b):
        return (a % b)


i0valid = False
i1valid = False
opvalid = False

while i0valid == False:
    try:
        i0 = float (input("First number: "))
        if (type (i0)) == int or float:
            p = float (i0)
            i0valid = True
            break
    except:
        print ("Invalid input")

while opvalid == False:
    fp0 = input ("Operation (Add, Sub, Mul, Div, Exp, Mod): ")
    fp1 = fp0.lower()
    if fp1 in ["add", "sub", "mul", "div", "exp", "mod"]:
        f = fp1
        opvalid = True
        break
    else:
        print ("Invalid operator")

while i1valid == False:
    try:
        i1 = float (input("Second number: "))
        if (type (i1)) == int or float:
            q = float (i1)
            i1valid = True
            break
    except:
        print ("Invalid input")

r = "Result:"

if f == "add":
    print (r, Cal.add (p,q))
if f == "sub":
    print (r, Cal.sub (p,q))
if f == "mul":
    print (r, Cal.mul (p,q))
if f == "div":
    print (r, Cal.div (p,q))
if f == "exp":
    print (r, Cal.exp (p,q))
if f == "mod":
    print (r, Cal.mod (p,q))
