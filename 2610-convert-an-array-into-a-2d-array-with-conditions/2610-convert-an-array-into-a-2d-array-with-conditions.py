class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        lookup = dict()
        result = [[] for i in range(0,len(nums))]
        dictionaryCount = 0
        
        for each in nums:
            if each in lookup:
                lookup[each] += 1
                result[lookup[each]].append(each)
            else:
                lookup[each] = 0
                result[0].append(each)
        
        lastFilled = 0
        for each in range(0,len(result)):
            if len(result[each]) == 0:
                lastFilled = each
                break
        if lastFilled != 0:
            return result[0:lastFilled]
        return result
                
                