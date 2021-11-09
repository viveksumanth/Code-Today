class Solution:
    def mySqrt(self, x: int) -> int:
        
        leftIdx = 0
        rightIdx = x
        
        '''
            [1,2,3,4,5,6,7,8]
            
            
        '''
        
        res = -1
        while(leftIdx <= rightIdx):
            
            midIdx = (leftIdx + rightIdx)//2
            
            if midIdx * midIdx <= x:
                res = midIdx
                leftIdx = midIdx + 1
            
            else: 
                rightIdx = midIdx - 1
        
        return res
                
        
        