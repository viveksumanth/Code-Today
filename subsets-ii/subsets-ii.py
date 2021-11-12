class Solution:
    
    
    '''
            
               []
            /       \
          1          2 
        /   \       /
     1,2    1,2   2,2
     /        \  
1,2,2       1,2,2
    

    '''
    def findSubsets(self, nums, ps, solutions, start):
        
        
        solutions.append(ps[:])
        
        if len(ps) == len(solutions):
            return
        
        for idx in range(start,len(nums)):
            if idx > start and nums[idx - 1] == nums[idx]:
                continue
                
            ps.append(nums[idx])
            self.findSubsets(nums, ps, solutions, idx+1)
            ps.pop()
        
        return solutions
    
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        solutions = self.findSubsets(nums,[],[],0)
        
        return solutions
        
