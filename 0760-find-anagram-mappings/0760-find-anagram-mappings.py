class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        lookup = dict()
        
        for i in range(0,len(nums2)):
            lookup[nums2[i]] = i
            
        for each in nums1:
            result.append(lookup[each])
        
        return result