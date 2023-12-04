class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxm = float("-inf")
        pointerA = 0
        pointerB = len(nums)-1

        while(pointerA < pointerB):
            currentSum = nums[pointerB] + nums[pointerA]
            
            if currentSum >= k:
                pointerB -= 1
            else:
                maxm = max(currentSum, maxm)
                pointerA += 1
        
        if maxm == float("-inf"):
            return -1
        
        return maxm