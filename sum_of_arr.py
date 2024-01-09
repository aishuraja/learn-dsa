"""
problem: Given an arr, find the sum of all elements in it
example: 
input: arr = [1, 2, 3, 4]
expected output: 10
"""

def s_arr (arr):
    a=0
    for i in range(len(arr)):
        a=a+arr[i]
    return a 
print(s_arr([1,2,3,4]))
