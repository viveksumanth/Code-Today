class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minmValue = float("inf")
        maxmValue = float("-inf")

        for each in nums:
            minmValue = min(minmValue, each)
            maxmValue = max(maxmValue, each)

        return (maxmValue - minmValue)*k