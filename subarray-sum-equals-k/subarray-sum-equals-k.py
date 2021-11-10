class Solution:   
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        '''

            numbers = [1,-1,1,1,1,1]   k = 3

            pairs = [1,-1,1,1,1] [1,1,1] [1,1,1] [-1,1,1,1,1]

            total = 4

            hm = {0:2, 1:2, 2: 1 ,3: 1}

            count = 2+2 = 4


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
    
        
        