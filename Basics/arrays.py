# creating 1D array 
# naive method

n = 5
arr = [0] * n
print(arr)

# using list comprehension 
n = 5
arr = [0 for i in range(n)]
print(arr)

# creating 2D array using naive method - not efficient 

rows , cols = (5,5)
arr = [[0]*cols]*rows
print(arr)

# using list comprehension - most efficient 

rows, cols = (5,5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

# attributes :

# .dtype - data type 
# .ndim - no of dimensions 
# .shape - eg:(2,3) - 2 rows 3 cols - gives tuple with no of rows and cols 
# .flatten() - convert 2D (multidimensional) to 1D array eg: ([1,2,3], [4,5,6]) = [1,2,3,4,5,6]

# matrix 

m = matrix ('1 2 3 ; 4  5 6 ; 7 8 9 ')
