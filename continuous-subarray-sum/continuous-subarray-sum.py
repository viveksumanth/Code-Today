class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        
        lookup = {
            5:0
            1:1
            
            
        }
        
        23%6 = 5
        25%6 = 1
        29%6 = 5
        [23,25,29]
        
        5 exists in lookup hence return True
        
        
        '''
        
        lookup = {
            0:-1
        }
        
        prefixSum = 0
        

        for idx in range(len(nums)):
            
            prefixSum += nums[idx]
            remainder = prefixSum % k

            if remainder in lookup and idx - lookup[remainder] > 1:

                return True
            
            elif remainder not in lookup :

                lookup[remainder] = idx

        return False
        