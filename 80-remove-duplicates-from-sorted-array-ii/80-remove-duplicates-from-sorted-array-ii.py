class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        hm = dict()
        
        for eachIdx in range(len(nums)):
            each = nums[eachIdx]
            if each not in hm:
                hm[each] = 1
            else:
                if hm[each] == 2:
                    nums[eachIdx] = '_'
                else:
                    hm[each] += 1
 
            
        fastPointer = 0
        slowPointer = 0
        count = 0
        for fastPointer in range(0,len(nums)):
            
            if nums[fastPointer]!= '_':
                nums[slowPointer],nums[fastPointer] = nums[fastPointer], nums[slowPointer]
                slowPointer += 1
                count += 1

        return count
            
            