import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        b a a b a
        
        a b a b a
        
        a: 
        
        a b a b
        
        '''
        lookup = Counter(s)
        k = 0
        
        organizedString = []
        heapArray = []
        
        for eachElement in lookup:
            
            heapq.heappush(heapArray, [-1 * lookup[eachElement], eachElement])
        
        
        while(len(heapArray) > 1):
            
            frequency,element = heapq.heappop(heapArray)
            frequency2,element2 = heapq.heappop(heapArray)
            
            organizedString.append(element)
            organizedString.append(element2)
            
            frequency = frequency + 1
            frequency2 = frequency2 + 1
            
            
            if -1 * frequency > 0:
                heapq.heappush(heapArray,[frequency,element])
            
            if -1 * frequency2 > 0:
                heapq.heappush(heapArray,[frequency2,element2])

        if len(heapArray):
            frequency,element = heapq.heappop(heapArray)
            organizedString.append(element)
        
        if len(organizedString) != len(s):
            return ''
        
        return ''.join(organizedString)
            