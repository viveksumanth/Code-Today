class Solution:
    
    def __init__(self):
        self.allResults = set()
        
    def combinationSumHelper(self,nums,target,ps):
        

#         if sum(ps) > target:
#             return
        
        if sum(ps) == target:
            newPs = tuple(ps)
            self.allResults.add(newPs)
            return 
        
        for eachIdx in range(len(nums)):
            
            currentNum = nums[eachIdx]
            
            if eachIdx > 0 and nums[eachIdx-1] == nums[eachIdx] or sum(ps) > target:
                continue
                
            self.combinationSumHelper(nums[eachIdx+1::],target,ps + [currentNum])
            
        return 
    
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.combinationSumHelper(candidates,target,[])
        
        return self.allResults