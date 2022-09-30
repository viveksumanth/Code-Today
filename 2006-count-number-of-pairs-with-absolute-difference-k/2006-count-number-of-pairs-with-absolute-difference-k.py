from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        prevIdx = 0
        '''
        
        [1,2,2,1]
        
         |
        [1,1,2,2]
             |
        
        a = k+b
        a = b-k
        
        '''
        lookup = defaultdict(int)
        count = 0
        
        for idx in range(0,len(nums)):
            
            if k+nums[idx] in lookup:
                count += lookup[k+num[idx]]
                
            elif nums[idx]-k in lookup:
                count += lookup[nums[idx]-k]
            
            lookup[nums[idx]] += 1
        
        return count
            