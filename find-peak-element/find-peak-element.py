class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
               |
        [1,2,1,3,5,6,4]
            
        '''
        leftIdx = 0
        rightIdx = len(nums) - 1

        while(leftIdx < rightIdx):

            middle = (leftIdx + rightIdx)//2
            
            if nums[middle] < nums[middle + 1]:
                leftIdx = middle + 1
            
            else:
                rightIdx = middle
        
        return leftIdx
        