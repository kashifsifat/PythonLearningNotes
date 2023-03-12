"""
Let's imagine a situation where a person helps at least two persons.
Then each of that two persons help another two persons and it continues...
How large the figure may become after it happens for few steps?
What might be the sum of people if it spreads as three per persons in every stages?
Let's try to calculate...
"""

per = int(input("Per person helps: "))
steps = int(input("Steps/stages continues: "))

total = 0

for i in range (1, steps+1):
    k = per ** i
    total += k

print ("Total =", total)
