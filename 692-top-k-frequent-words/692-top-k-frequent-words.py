from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        lookup = Counter(words)
        newList = []
        result = []
        
        for eachKey in lookup:
            newList.append([-1*lookup[eachKey],eachKey])
        
        heapq.heapify(newList)
        
        
        for eachWordIdx in range(0,k):
            frequency,currentWord = heapq.heappop(newList)
            
            result.append(currentWord)
        
        return result
        
        
        
        
                
        
        