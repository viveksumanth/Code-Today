class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) > 2:
            prev = nums[0] - nums[1]
            
        count = 1
        totalSlices = 0
        
        for eachIdx in range(2,len(nums)):
            curr = nums[eachIdx - 1] - nums[eachIdx]

            if prev != curr:
                count += 1
                totalSlices += ((count-2)*(count-1))//2
                prev = curr
                count = 1
                
            else: 
                count += 1
        
        count += 1
        totalSlices += ((count-2)*(count-1))//2
        
        return totalSlices
        
                    
                
            
        
        
        