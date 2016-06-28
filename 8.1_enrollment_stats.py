''' Real Python
    8.1 Assignment: List of lists
    Define a function, enrollment_stats() , that takes, as an input, a list of lists where each individual list contains three elements:
    (a) the name of a university,
    (b) the total number of enrolled students, and
    (c) the annual tuition fees.
    
'''

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def mean(values_list):
    ''' return the mean of the values in the list '''
    somme = 0
    for value in values_list:
        somme += value

    return int(somme / len(values_list))

def median(values_list):
    ''' return the median of all the values in the list '''
    number_element = len(values_list)
    values_list.sort()
    return values_list[int(number_element/2)]

#   [TODO] even and odd calculation differs for median
#    if number_element % 2 == 0: #even list
    

def enrollment_stats(universities_list):
    
    stats = [ [], [] ]

    for university in universities_list:
        stats[0].append(university[1])  # students
        stats[1].append(university[2])  # tuition fees

    return stats

        
### MAIN

universities_stats = enrollment_stats(universities)

print('*'*25)
print('Total students:  {} \nTotal tuition: $ {} \n'.format(sum(universities_stats[0]), sum(universities_stats[1]),))
print('Student mean:   {} \nStudent median: {} \n'.format(mean(universities_stats[0]), median(universities_stats[0])))
print('Tuition mean:   $ {} \nTuition median: $ {}'.format(mean(universities_stats[1]), median(universities_stats[1])))
print('*'*25)
