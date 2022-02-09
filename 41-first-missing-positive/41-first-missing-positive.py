class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        x = 0
        index = 0
        '''
        
        [3,1,2]
        
        '''
        
        while(x<len(nums)):
            
            if nums[x] <= 0:
                del nums[x]
                continue
            x = x+1 
        
        if len(nums) == 0:
            return 1
        
        
        while(index < len(nums)):
            
            currentNumber = nums[index] - 1
            
            if 0 <= currentNumber < len(nums) and nums[index] != nums[currentNumber]:
                nums[index],nums[currentNumber] = nums[currentNumber],nums[index]
                
            else:
                index += 1
                

        for eachIndex in range(0,len(nums)):

            if nums[eachIndex] != eachIndex + 1:
                return eachIndex + 1
        return max(nums) + 1
                
                
            
        
        
            
            
                
            
            