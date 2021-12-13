class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
            1 1 1 2 3 1 
                  l r
            
        '''
        leftIdx = 0
        rightIdx = len(nums) - 1

        while(leftIdx < rightIdx):

            middle = (leftIdx + rightIdx)//2
            
            if nums[middle] > nums[middle + 1]:
                rightIdx = middle
            
            else:
                leftIdx = middle + 1
        
        return leftIdx
        