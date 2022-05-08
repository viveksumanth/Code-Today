class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        numberOfGreater = 0
        
        for each in range(1,len(nums)):
            if nums[each-1] > nums[each]:
                numberOfGreater += 1

                if numberOfGreater > 1:
                    return False
                
                
                if each < 2 or nums[each-2] <= nums[each]:
                    nums[each-1] = nums[each]
                else:
                    nums[each] = nums[each-1]

        return True