from collections import Counter
class Solution:
    
    def generateChildren(self,word,words):
        neighbours = []
        
        for i in range(len(word)):
            newWord = list(word[:])
            newWord.pop(i)
            newWord = ''.join(newWord)
            if newWord in words:
                neighbours.append(newWord)
        
        return neighbours
            
            
    
    def DFS(self, word, words, seen):
        
        if len(word) == 0:
            return 0
        
        neighbours = self.generateChildren(word,words)
        
        depth = 0
        
        for neighbour in neighbours:
            
            if neighbour not in seen:
                
                depth = max(depth, self.DFS(neighbour, words, seen))
                seen[neighbour] = depth
            
            else:
                
                depth = seen[neighbour]
        
        return depth + 1
                
            
        
    def longestStrChain(self, words: List[str]) -> int:
        
        words = Counter(words)
        seen = { }
        longestChain = 1
        
        for word in words:
            longestChain = max(longestChain, self.DFS(word, words, seen))
        
        return longestChain
            
        