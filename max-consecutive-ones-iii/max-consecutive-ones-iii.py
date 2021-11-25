class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        '''
                 |
        [1,1,1,0,0,0,1,1,1,1,0] maxm tolerate = 2
                   |
         
        maximum = 5
        
        using two pointers and sliding window
        
        first pointer moves till the condition is satisfied where as other pointer starts when condition is sastisfied 
        
         |
        [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] k = 3
         |
        '''

        validZeros = k
        pointerB = 0
        maxLength = 0
        
        for idx in range(0,len(a)):
            
            if a[idx] == 0:
                validZeros -= 1
            
            if validZeros < 0:
                while(a[pointerB] != 0):
                    pointerB += 1
                validZeros += 1
                pointerB+= 1
            
            maxLength = max(maxLength, idx - pointerB + 1 )
            # print(idx,pointerB,validZeros,maxLength)
        return maxLength
            
            
                    
            
        