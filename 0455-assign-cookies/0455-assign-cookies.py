class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
               |
        g = [1,2,3]
             |
        s = [1,1,2]
        
        '''
        child = 0
        g.sort()
        s.sort()
        gPointer = 0
        sPointer = 0
        
        while(gPointer < len(g) and sPointer < len(s)):
            if s[sPointer] >= g[gPointer]:
                child += 1
                sPointer += 1
                gPointer += 1
            else:
                sPointer += 1
    
        return child