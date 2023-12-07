class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximumReachableDistance = 0
        if len(nums) == 1:
            return True
        
        if nums[0] == 0:
            return False
        
        for eachIdx in range(0,len(nums)):
            if eachIdx > maximumReachableDistance:
                return False
            
            reachable = eachIdx + nums[eachIdx]
            
            if reachable >= len(nums)-1:
                reachable = len(nums)-1
                
            maximumReachableDistance = max(maximumReachableDistance, reachable)

            if maximumReachableDistance == len(nums)-1:
                return True
        
        return False
        