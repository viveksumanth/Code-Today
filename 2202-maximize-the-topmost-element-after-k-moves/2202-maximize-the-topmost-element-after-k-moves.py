class Solution:
    
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        maxmElement = float('-inf')

        if k > len(nums):
            
            if len(nums) == 1 and k%2==0:
                return nums[0]
            
            elif len(nums) == 1:
                return -1
            
            return max(nums) 
        
        if k == 0:
            return nums[0]
        
        if k == 1:
            if len(nums) == 1:
                return -1
            else:
                return nums[1]
            
        if k > 1:
            
            for idx in range(0,k-1):
                maxmElement = max(maxmElement,nums[idx])

            if k <= len(nums)-1:
                maxmElement = max(nums[k],maxmElement)
            
            return maxmElement
                
            
        
            
        
        