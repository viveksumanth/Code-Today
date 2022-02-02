

from collections import Counter


class Solution:
    def findAnagrams(self, string: str, tem: str) -> List[int]:
        
        windowSize = len(tem)
        tem = Counter(tem)
        result = []
        newHm = dict()
        current = 0
        
        for eachIdx in range(0,len(string)):

                
            while(eachIdx - current + 1 > windowSize):
                letter = string[current]
                
                if letter in newHm:
                    if newHm[letter] > 1:
                        newHm[letter] -= 1
                    else:
                        del newHm[letter]
                
                current = current + 1
            
            letter = string[eachIdx]
            
            if letter in newHm:
                newHm[letter] += 1
            
            else:
                newHm[letter] = 1
                
            if newHm == tem:
                result.append(abs(windowSize - eachIdx - 1))  
                

        return result
                
                
                
            
        
        
        
        