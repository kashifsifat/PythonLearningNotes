floatNumber = 1.9876
fn = 1.70257638
#fn = float (input ())

print ("%.7f" %fn)

print("%.2f" %floatNumber, "%.2f" %fn)

print ("%.2f" %fn)

print ("%.3f" %fn)

print ("%.4f" %fn)

"""
A little note:
" " (quotation mark)
%.3f (percent dot (decimal point) f) without space [inside of the quotation mark]
%variable name [outside of the quotation mark]
"""

#This program outputs as below:
#1.7025764
#1.99 1.70
#1.70
#1.703
#1.7026
#This program can also be used for formatting float number from user input with some slight modifications.
