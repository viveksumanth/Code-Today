class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        '''
        store the sorted nums in nums2
        check the posistions of the nums and nums2 
        first element to be diffrent - last element to be different
        
        '''
        nums2 = sorted(nums)
        pointers = []

        for each in range(0,len(nums)):
            
            if nums[each] != nums2[each]:
                pointers.append(each)
        
        if len(pointers):
            return pointers[-1] - pointers[0] + 1
        return 0
                
        