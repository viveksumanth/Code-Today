from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = Counter(words)
        wordHeap = []
        result = []
        
        for eachWord in wordCount:
            heapq.heappush(wordHeap,[-1*wordCount[eachWord], eachWord])
                                              
        for i in range(0,k):
            
            count,word = heapq.heappop(wordHeap)
            result.append(word)
        
        return result
                                     
            
            
            
        
        