class Solution:
    def __init__(self):
        self.allSets = []
        
    def makeSubsets(self,nums,currentSet,start):
        self.allSets.append(currentSet[:])
        
        if len(currentSet) == len(nums):
            return 
        
        for each in range(start,len(nums)):
            currentSet.append(nums[each])
            self.makeSubsets(nums,currentSet,each+1)
            currentSet.pop()
        
        return 
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        currentSet = []
        self.makeSubsets(nums,currentSet,0)
        
        return self.allSets