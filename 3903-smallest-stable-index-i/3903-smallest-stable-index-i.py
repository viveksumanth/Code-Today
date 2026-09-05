class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        result = float('inf')
        index = -1
        for i in range(0, len(nums)):
            curResult = max(nums[:i+1]) - min(nums[i:])
            newResult = min(curResult, result)
            if newResult <= k:
                index = i
                return index
        return index

        