"""
Problem: Given an arr and a target value, find if the sum of the array elemts is eqauls to target value
example: arr = [1,2,3,4] target = 8
expected outout: False becase sum of all ele iof arr is 10 and target is 8
"""

def check_sum(arr, target):
    a=0
    for i in range(len(arr)):
        a=a+arr[i]
    if a == target:
        return True 
    else:
        return False
    

print(check_sum([1,2,3,4], 10))