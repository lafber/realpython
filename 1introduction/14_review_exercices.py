''' Real Python
Review exercises
'''

### Module(s) importation ###
from numpy import array, arange, reshape, vstack, dot

### Functions ###

### Parametrage ###

############
### MAIN ###
############

# chapter 14 review ex 1 : Create a 3 x 3 NumPy array named first_matrix that 
# includes the numbers 3 through 11 by using arange() and reshape()
print('-'*10, "Review exercice 1 chapter 14", '-'*10)

first_matrix = arange(3,12)
first_matrix = first_matrix.reshape(3,3)
print(first_matrix)

# chapter 14 review ex 2 : Display the minimum, maximum and mean of all entries in first_matrix
print('-'*10, "Review exercice 2 chapter 14", '-'*10)

print("First Matrix minimum is {}, maximum is {} and mean is {},".format(first_matrix.min(), first_matrix.max(), first_matrix.mean()))



# chapter 14 review ex 3 : Square every entry in first_matrix using the ** 
# operator, and save the results in an array named second_matrix
print('-'*10, "Review exercice 3 chapter 14", '-'*10)

second_matrix = first_matrix**2
print(second_matrix)

# chapter 14 review ex 4 : Use vstack() to stack first_matrix on top of 
# second_matrix and save the results in an array named third_matrix
print('-'*10, "Review exercice 4 chapter 14", '-'*10)

third_matrix = vstack([first_matrix, second_matrix])
print(third_matrix)

# chapter 14 review ex 5 : Use dot() to calculate the dot product of third_matrix by first_matrix
print('-'*10, "Review exercice 5 chapter 14", '-'*10)

print("Le produit scalaire de la matrice 1 et 2 est \n{}".format(
    dot(first_matrix,second_matrix)))
    
    
# chapter 14 review ex 6 : Reshape third_matrix into an array of dimensions 3 x 3 x 2
print('-'*10, "Review exercice 5 chapter 14", '-'*10)
third_matrix = third_matrix.reshape(3,3,2)
print(third_matrix)