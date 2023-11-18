class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        pointerA = 0
        pointerB = 0
        result = 1
        currentSum = 0
        for pointerB in range(0, len(nums)):
            currentSum += nums[pointerB]
            windowLength = pointerB - pointerA+1
            while (nums[pointerB]*windowLength > currentSum+k):
                currentSum = currentSum - nums[pointerA]
                windowLength -= 1
                pointerA += 1
            result = max(result, windowLength)
        
        return result
            