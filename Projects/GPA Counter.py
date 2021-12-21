print("Assalamu Alaikum! This program is for calculating your GPA. Specially for HSC exams upto 2013 batch.")
print ("Enter the Grade Point of each subjects")
ben = float(input("Bengali: "))
eng = float(input("English: "))
e1 = float(input("First Elective Subject: "))
e2 = float(input("Second Elective Subject: "))
e3 = float(input("Third Elective Subject: "))
# Used e1, e2, e3 for three elective subjects.

fs_fv = float(input("Fourth Subject: "))
# Used 'fs_fv' as variable name to indicate "Fourth Subject Face Value". Users shouldn't need to worry about more calculation.

if fs_fv >  2:
    fs_av = fs_fv-2
else:
    fs_av = 0
# As it was the rule - students who got grade point 2 or more in their fourth subject were rewarded with the face value-2 points.
# Used 'fs_av' as variable name to indicate the "Fourth Subject Actual Value". That means, calcualtion is done! Cheers!

if ben and eng and e1 and e2 and e3 != 0:
    print ("Result: Passed")
else:
    print ("Result: Failed")
# Used for primarily showing 'Passed' or 'Failed' as 'Result'.

GPA = (ben+eng+fs_av+e1+e2+e3)/5
if GPA > 5:
    print ("Your GPA is: 5.0")
else:
    print("Your GPA is: ", GPA)
# This is the final GPA. Average of the grade points of all subjects. Note that, we are counting the substracted value of fourth subject.
