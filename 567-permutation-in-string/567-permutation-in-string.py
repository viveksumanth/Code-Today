from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''
        
        a:1
        b:1
        
    
        i:1
        
        
        '''
        pointerA = 0
        lookup = Counter(s1)
        newHm = dict()
        # print(s1)
        for eachIdx in range(0,len(s2)):
            
            letter = s2[eachIdx]
            
            if letter not in newHm:
                newHm[letter] = 1
            else:
                newHm[letter] += 1
            
            # print(newHm)
            if newHm == lookup:
                return True
                
            if eachIdx - pointerA + 1 >= len(s1):
                delLetter = s2[pointerA]
                
                newHm[delLetter] -= 1
                
                if newHm[delLetter] == 0:
                    del newHm[delLetter]
                    
                pointerA+= 1
        
        if newHm == s1:
            return True
        return False
                
            
            
            
            