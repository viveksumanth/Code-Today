#the subsequnce should contain all distinct values and characters set should be consequitve #irrespective of its order

from collections import Counter
class Solution:
    
#     def longestConsecutive(self, nums: List[int]) -> int:
#         pass
    
 
    

# Using Recursion and a for loop works but results in TLE
# Time Complexity = O(n*n)
        
#     def checker(self,check,count):
        
#         if check in self.hm.keys():
#             count = count + 1
#             return self.checker(check - 1, count)
#         else:
#             return count

        
#     def longestConsecutive(self, nums: List[int]) -> int:
#         self.nums = nums
#         self.hm = Counter(nums)
#         maxm = float('-inf')
        
#         if len(nums) == 0:
#             return 0
        
#         for i in range(0,len(nums)):
            
#             count = self.checker(nums[i],0)
#             maxm = max(maxm,count)
#         return maxm
    


        
    def longestConsecutive(self, nums: List[int]) -> int:
        self.nums = nums
        self.hm = Counter(nums)
        maxm = float('-inf')
        
        if len(nums) == 0:
            return 0
        
        for i in range(0,len(nums)):
            count = 0
            k = nums[i]
            
            # if there exists a value lower than current in hashmap 
            #then we can compute from that rather than counting for that.
            # Mind == Fuck
            
            if k - 1 not in self.hm.keys():
                print(k-1)
                while(k in self.hm.keys()):
                    count = count + 1
                    k = k + 1

            maxm = max(maxm,count)
            
        return maxm