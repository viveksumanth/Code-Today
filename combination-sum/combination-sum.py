class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def dfs(subsolution, start, current,solutions):
            
            if current == 0:
                solutions.append(subsolution[:])
                return
            
            for i in range(start,len(candidates)):
                
                if current - candidates[i] >= 0:
                    
                    dfs(subsolution + [candidates[i]],i,current-candidates[i],solutions)
            
            return solutions
        
        return (dfs([],0,target,[]))
        
    
    
        