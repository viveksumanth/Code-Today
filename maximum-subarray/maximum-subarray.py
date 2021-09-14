#algoexpert - Kadane's Algorithm 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum = 0
        cursum = 0
        allmax = float('-inf')
        for i in nums:
            cursum = cursum +i
            maxsum = max(i,cursum)
            cursum = maxsum
            allmax = max(allmax,maxsum)
        
        return allmax
            
                