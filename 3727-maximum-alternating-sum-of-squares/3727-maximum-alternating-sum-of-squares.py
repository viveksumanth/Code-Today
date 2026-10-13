class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        numsSquare = [each*each for each in nums]
        numsSquare.sort(reverse = True)
        
        if len(nums)%2 == 0:
            half = len(nums)//2
        else: 
            half = len(nums)//2
            half += 1

        sumPart = numsSquare[0:half]
        subPart = numsSquare[half::]
        return sum(sumPart) - sum(subPart)
