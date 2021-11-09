class Solution:
    def findRange(self,nums,leftIdx, rightIdx, target,direction):
        
        while(leftIdx <= rightIdx):
            
            middleIdx = (leftIdx + rightIdx)//2
            
            if nums[middleIdx] < target:
                leftIdx = middleIdx + 1
            
            elif nums[middleIdx] > target:
                rightIdx = middleIdx - 1
            
            else:
                if direction == "left":
                    
                    if middleIdx == 0 or nums[middleIdx - 1] != target:
                        return middleIdx
                    
                    else:
                        rightIdx = middleIdx - 1
                
                if direction == "right":
                    
                    if middleIdx == len(nums) - 1 or nums[middleIdx + 1] != target:
                        return middleIdx
                    else:
                        leftIdx = middleIdx + 1
            
        return -1
            
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        leftIdx = 0
        rightIdx = len(nums) - 1
        
        leftRange = self.findRange(nums, leftIdx, rightIdx, target, "left")
        rightRange = self.findRange(nums, leftIdx, rightIdx, target, "right")
        
        return [leftRange, rightRange]
        
        
        