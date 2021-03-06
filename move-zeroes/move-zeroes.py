class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        zerocount = 2
        
        1,0,2,0,4,0,2,3,0 
        
        1,2,4,2,3,0,2,3,0 
                          l 
                r
        """
        
        fastPointer = 0
        slowPointer = 0
        
        for fastPointer in range(0,len(nums)):
            
            if nums[fastPointer]!= 0:
                nums[slowPointer],nums[fastPointer] = nums[fastPointer], nums[slowPointer]
                slowPointer += 1

    
                

                
                