class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minm = float("inf")

        for i in range(0, len(nums)):
            if nums[i] == target:
                minm = min(minm, abs(i-start))
        
        return minm
        