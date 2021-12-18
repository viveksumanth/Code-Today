class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
        
        nums1 = [4,1,2]
        
        nums2 = [1,3,4,2]
        
        lookup = {
            1 : 3
            3 : 4
            4 : -1
            2 : -1 
        }
        
        result = [-1,3,-1]
        
        nextGreaterElements = [3,4,-1,-1]
        
        '''
        
        lookup = {}
        stack = []
        result = []
        
        for idx in range(0,len(nums2)):
            
            while stack and stack[-1] < nums2[idx]:
                currentNumber = stack.pop()
                lookup[currentNumber] = nums2[idx]
            stack.append(nums2[idx])
        
        for each in stack:
            lookup[each] = -1
        
        for eachNum in range(0,len(nums1)):
            nums1[eachNum] = lookup[nums1[eachNum]]
        
        return nums1
                
        
        