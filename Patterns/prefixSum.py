# originalArray = [ 1,2,4,5,3]
def originalArray():
    n = len(originalArray)
    newArray = [0]*n   # it will appeear as newArray = [0,0,0,0,0]
    newArray[0] = originalArray[0]
    for i in range(1,n):
        # originalArray[i] + newArray[i-1] - basic logic to have the calculated values in newArray
        a = originalArray[i] + newArray[i-1] 
        newArray.insert(i,a)

    return newArray

# created a newArray 

# use the formula if need to access the index :  newArray[j] - newArray[i-1] and it has O(1) constant time. 

