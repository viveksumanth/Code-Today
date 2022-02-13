class Solution:
    def __init__(self):
        self.solutions = []
        
    def dfs(self,nums,startIdx,ps):

        self.solutions.append(ps)
        
        if startIdx == len(nums):
            return
        
        
        for eachIdx in range(startIdx,len(nums)):
            
            self.dfs(nums,eachIdx+1,ps+[nums[eachIdx]])
        
        return 
    
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        self.dfs(nums,0,[])
        return self.solutions