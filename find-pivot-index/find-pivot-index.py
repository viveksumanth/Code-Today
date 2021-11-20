class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        
        [2,1,-1]
        
        sum = 2
        
        when totalSum - num == prefixSum then nums index is prefix sum
        
        totalsum = 2
        prefixSum = 2
        pivot = 0
        
        [1,7,3,6,5,6]
        
        sum = 28
        
        prefixSum = 1   28
        prefixSum = 8.  28 - 1 = 27
        prefixSum = 11. 28 - 7 = 20
        prefixSum = 17  20 - 3 = 17
        
        '''
        
        totalSum = sum(nums)
        prefixSum = 0
        prevnum = 0
        
        for idx in range(0,len(nums)):
            prefixSum += nums[idx]
            totalSum = totalSum - prevnum
            if prefixSum == totalSum:
                return idx
            else:
                prevnum = nums[idx]
        
        return -1
        