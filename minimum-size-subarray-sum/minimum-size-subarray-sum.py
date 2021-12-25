class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pointerA = 0
        pointerB = 0
        sumSoFar = 0
        minmSubArray = float('inf')

        for idx in range(pointerA, len(nums)):
            sumSoFar += nums[idx]

            while(sumSoFar >= target):
                minmSubArray = min(minmSubArray, idx - pointerB+ 1)
                sumSoFar -= nums[pointerB]
                pointerB = pointerB + 1

        if minmSubArray == float('inf'):
            return 0

        return minmSubArray

        