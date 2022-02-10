class Solution:   
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        '''

            numbers = [1,-1,1,1,1,1]   k = 3
            
            [0,3,4,3,....]
    
            pairs = [1,-1,1,1,1] [1,1,1] [1,1,1] [-1,1,1,1,1]

            total = 4
            
            count = 0
            
            hm = {0: 1, 1: 1,   }
            
            prefixSum = 0
             

        '''
        
        count = 0
        lookup = {0:1}
        prefixSum = 0
        
        for i in range(0,len(nums)):

            prefixSum += nums[i]
            
            if prefixSum - k in lookup:
                count = count + lookup[prefixSum-k]

            if prefixSum in lookup:
                lookup[prefixSum] += 1
            else:
                lookup[prefixSum] = 1
        
        
        return count   
    
        
        