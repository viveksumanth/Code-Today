class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
    
        result = []
        for i in nums:
            if nums[abs(i) - 1] < 0:
                result.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1
        
        return result