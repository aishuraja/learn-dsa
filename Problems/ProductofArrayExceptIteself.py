class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two passes 
        # [1,2,4,6] 
        # leftArr = [0]*n
        # RArr = [0]*n
        # leftmultiplier = 1
        # Rightmultiplier = 1

        n = len(nums)
        leftArr = [0] * n
        RightArr = [0]* n
        left_mul = 1
        right_mul = 1


        for i in range(0, n):
            j = -i -1 # set the j to last index in nums 
            leftArr[i] = left_mul
            RightArr[j] = right_mul
            left_mul = left_mul * nums[i]
            right_mul = right_mul * nums[j]

        return [l*r for l, r in zip(leftArr, RightArr)]