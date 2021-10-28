class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # find the subarray whose sum is greater than or equal to the target sum
        minSize = float('inf')
        cSum = 0
        pointerA = 0
        pointerB = 0
        # move pointer b to correct posistion
        """
        2 3 1 2 4 3   target 7 minsum = inf cursum = 0
        csum = 2, 5, 6 8
        pointer b = 3
        minsize = 4
        pointer a = 0
        
        2 3 1 2 4 3
        |     |
        """
        for pointerB in range(0,len(nums)):
            if cSum < target:
                cSum = cSum + nums[pointerB]
            
            while(cSum >= target):
                minSize = min(minSize , pointerB - pointerA+1)
                # move pointerA until >= target condition is violated
                cSum = cSum - nums[pointerA]
                pointerA += 1
                
            
        if minSize == float('inf'):
            return 0
        return minSize
        