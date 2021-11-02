# quick select
class Solution:
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]
        
    def quickselect(self, startIdx, endIdx, nums,k):
        pivotIdx = startIdx
        leftIdx =  startIdx + 1
        rightIdx = endIdx
        
        while(leftIdx <= rightIdx):
            
            if nums[leftIdx] > nums[pivotIdx] and nums[rightIdx] < nums[pivotIdx]:
                self.swap(leftIdx, rightIdx, nums)
            
            if nums[leftIdx] <= nums[pivotIdx]:
                leftIdx += 1
            
            if nums[rightIdx] >= nums[pivotIdx]:
                rightIdx -= 1
            
        self.swap(rightIdx, pivotIdx, nums)
        
        posistion = len(nums) - k

        if rightIdx == posistion:
            return 
        
        if posistion < rightIdx:
            #move left from posistion
            self.quickselect(startIdx, rightIdx - 1, nums,k)
            
        if posistion > rightIdx:
            #move right
            self.quickselect(rightIdx + 1, endIdx, nums,k)
        
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        kthLargest = self.quickselect(0, len(nums) - 1, nums,k)

        return nums[len(nums) - k]
        
        
        