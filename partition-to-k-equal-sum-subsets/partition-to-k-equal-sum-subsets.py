class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 0 or sum(nums)%k != 0:
            return False
        
        target = sum(nums)//k
        sums = 0
        used = [False]*len(nums)
        flag = False
        
        def dfs(start,nums, used, target, sums,k):

            if k == 1:
                return True 

            if sums == target:
                
                k = k - 1
                
                return dfs(0,nums,used,target,0,k)
            
            for i in range(start,len(nums)):
                
                if used[i] == False:
                    used[i] = True
                    
                    if dfs(i+1,nums,used,target,sums+nums[i],k):
                        return True
                    
                    used[i] = False
            
            return False
        
        return dfs(0,nums, used, target, sums,k)

            
        