class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
            prefixSum = 0
            lookup = {0:1}
            subarrayCount = 0

            for num in nums:
                prefixSum += num
                remainder = (prefixSum % k)
                
                if remainder in lookup:
                    subarrayCount += lookup[remainder]
                    lookup[remainder] += 1
                else:
                    lookup[remainder] = 1
                

            return subarrayCount
        