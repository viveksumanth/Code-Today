class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        best = now = sum(nums[:k])
        maxAvg = best/k
        for i in range(k,len(nums)):
            now += nums[i] - nums[i-k]
            maxAvg = max(maxAvg, now/k)
        return maxAvg
            
            