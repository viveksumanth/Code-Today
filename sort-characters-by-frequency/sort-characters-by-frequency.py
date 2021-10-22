# sort by frequency heap

import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        maxheap = []
        result = []
        
        for i in freq:
            heapq.heappush(maxheap, (freq[i]*(-1),i))
        
        # print(maxheap)
        for i in range(len(maxheap)):
            sub = heapq.heappop(maxheap)
            result.append(-1* sub[0]*sub[1])
        
        return ''.join(result)
            
        
        
            
        
        
        
        
        
        
        