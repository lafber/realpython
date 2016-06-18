''' Real Python
    7.5 review excercice 2   
    Combine a for loop over a range() of numbers with the continue keyword to print every number from 1 through 50 except for multiples of 3; you will need to use the % operator.
'''

for i in range(1,51):
    if i % 3 == 0:
        continue
    print(i)

