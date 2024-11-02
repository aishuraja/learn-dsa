"""
Problem: Given an array with Integer, if all elements are even, Return true, else retrun false
Example: arr = [2,3,8,6]
output: False becasue 3 is odd

arr = [2,6,8,10]
output:  True
"""

def check_all_ele_even(arr):
    for i in range(len(arr)):

        if arr[i]%2!= 0:

            return False
        
    return True


print(check_all_ele_even([2,3,4,6]))
print(check_all_ele_even([2,10,4,6]))

