# Array Rotation:

# It is very simple. The basic steps are:
# * Need to store 1st element in tremperory variable 
# * Once its done shift the remaining elements towards left 
# * Then place the temporary variable at the last index of the array 
# * Print it . 

# This can be achieved with for loop , 

# I/P: [1,2,3,4,5]
# Op: [3,4,5,1,2]
# k =3 [shifting element]

## left rotation 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(0,k):
            temp= nums[0]
            for j in range(0,len(nums)-1):
                nums[j] = nums[j+1]
                nums[len(arr)-1]= temp
        for i in range(0,len(nums)):
            print(nums[i])

## right rotation: same as left rotation (opposite)
            
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(0,k):
            temp = nums[len(nums)-1]
            for j in range(len(nums)-1,0,-1):
                nums[j] = nums[j-1]
                nums[0] = temp 
        for i in range(0,len(nums)):
            print(nums[i])

            

