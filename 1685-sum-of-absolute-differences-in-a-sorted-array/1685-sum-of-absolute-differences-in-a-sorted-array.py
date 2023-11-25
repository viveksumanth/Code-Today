class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        prefixSumArray = list()
        prefixSum = 0
        for each in nums:
            prefixSum += each
            prefixSumArray.append(prefixSum)
            
        sufixSumArray = list()
        sufixSum = sum(nums)
        for each in nums:
            sufixSumArray.append(sufixSum)
            sufixSum -= each
    
        result = list()
        numsLen = len(nums)
        for i in range(0,len(nums)):
            resultSum = ((i+1)*nums[i]) - prefixSumArray[i] - ((numsLen-i)*nums[i])+sufixSumArray[i]
            result.append(resultSum)
        
        return result
            