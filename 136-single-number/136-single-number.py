class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        '''
        
        1,1,2,2,4
        
        
        '''
        for i in range(1,len(nums),2):
            if nums[i-1] != nums[i]:
                return nums[i-1]
        
        if len(nums)%2 == 1:
            return nums[-1]
        
        