class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        findMax = [0 for i in range(0,len(nums))]
        findMax[0] = nums[0]
        findMax[1] = max(nums[0],nums[1])
        
        for idx in range(2,len(nums)):
            findMax[idx] = max(nums[idx] + findMax[idx-2], findMax[idx-1])
        

        return findMax[-1]
    
            
