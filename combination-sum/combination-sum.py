class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(start,candidates, target, subsolution, solutions):
            # print(subsolution)
            if sum(subsolution) == target:
                answer = sorted(subsolution)
                if answer not in solutions:
                    solutions.append(answer)
            
            for i in range(start,len(candidates)):
                subsolution.append(candidates[i])
                
                if sum(subsolution) <= target:
                    dfs(start,candidates, target, subsolution,solutions)
                
                subsolution.pop()
            
            return solutions
        
        return (dfs(0,candidates, target, [], []))
        
    
    
        