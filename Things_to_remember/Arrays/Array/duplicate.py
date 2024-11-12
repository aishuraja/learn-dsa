# Problem: check list for duplicate 
# solution: O(n2) - 2 for loops | O(n) - using sets 
# iterate through the list and create set

# sets are fast and does not contain duplicates 

nums = [1,2,2,3]

seen = set()
for num in nums:
    if num in seen:
        print("true, has duplicates")
    seen.add(num)
    print("seen val:", seen) 
#retrun false