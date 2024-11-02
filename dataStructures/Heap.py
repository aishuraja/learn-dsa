# Heap - kind of binary tree used to sort , find min and max 
# Has 2 heaps - min heap and max heap 
# min heap - the parent node has min value than its children 
# max heap - the parent node has max value than its children 
# Heapify - this function is used to build an heap (make an arr into an heap )


# Build Min heap (Heapify)
# Time: O(n) , Space: O(1)
arr = [-3, 2, 10, 7, 9, 6, -2, 5]
# to satisy the heap prop import heapq lib 
import heapq
heapq.heapify(arr)   # this heapfiy makes the arr list to an heap 
print(arr)


# Heap Push (Insert element)
# Time: O(log n)
heapq.heappush(arr, 4)  # here inserting 4 into heap `arr` not into array arr as we build heap in before step 
print(arr)


#Heap Pop (Extract min) - gets the current min value 
# time: O(log n )
b = heapq.heappop(arr)  # pop removes the top element here which is `-3` here its min heap so the min value will be at the top node 
print(arr)


# Heap Sort 
# Time: O( n log n )
# Space: O(n)
def heapsort(nums):
    heapq.heapify(nums)
    newList = [0] * len(nums)
    for i in range(len(nums)):
        minn = heapq.heappop(nums)
        newList[i] = minn

    return newList
heapsort([1,3,10,-1,8,5,4])

