"""
Problem: Given two arrays arr1 and arr2, find if the sum of the two arrays are equal
Example:
arr1 = [1,2,3,4]
arr2 = [5,5]

Expected output: True

arr1 = [7,11]
arr2 = [6,7]

Expected output: False
"""


# Return True/False
def check_same_sum(arr1, arr2):
    a=0
    b=0
    for i in range(len(arr1)):
        a=a+arr1[i]
        print("this is a:", a)
        
    for j in range(len(arr2)):
        b=b+arr2[j]
        print("this is b:" ,b)
    if a==b:
        return True

    return False


print(check_same_sum([1,2,3,4], [5,5]))
print(check_same_sum([1,4], [5,1]))

