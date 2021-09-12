from collections import Counter
class Solution:
    def interchangeableRectangles(self, rect: List[List[int]]) -> int:
        

        sums = 0
        for i in range(0,len(rect)):
            rect[i] = (rect[i][0]/rect[i][1])
        
        hm = Counter(rect)

        for i in hm.keys(): 
            if hm[i] >= 2:
                sums = sums + (hm[i] * (hm[i]-1))//2
                
        return sums