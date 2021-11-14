class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        pointerB = n - 1
        pointerA = m - 1
        insertPointer = m + n - 1
        
                
        while(pointerB >= 0 and pointerA >= 0):
            
            if nums1[pointerA] < nums2[pointerB]:
                nums1[insertPointer] = nums2[pointerB]
                insertPointer -= 1
                pointerB -= 1
            
            elif nums1[pointerA] >= nums2[pointerB]:
                
                nums1[pointerA], nums1[insertPointer] = nums1[insertPointer],nums1[pointerA]
                

                pointerA -= 1
                    
                insertPointer -= 1
        
        if pointerB >= 0:
            nums1[:insertPointer+1] = nums2[:pointerB+1]
                
                