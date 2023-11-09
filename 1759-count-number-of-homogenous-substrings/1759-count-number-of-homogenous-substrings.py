class Solution: 
        
    def calculateHomogenousSubStrings(self, subStringLength):
        return subStringLength* (subStringLength + 1) //2 
                
    def countHomogenous(self, s: str) -> int:
        pointerA = 0
        pointerB = 0
        homogenousSubStrings = 0
        
        while(pointerA < len(s)):
            
            if s[pointerA] != s[pointerB]:
                subStringLength = pointerA - pointerB
                homogenousSubStrings += self.calculateHomogenousSubStrings(subStringLength)
                pointerB = pointerA
            pointerA += 1
        
        #last String
        subStringLength = pointerA - pointerB
        subStringChar = s[pointerA-1]
        homogenousSubStrings += self.calculateHomogenousSubStrings(subStringLength)
        return homogenousSubStrings % (10**9 + 7)
                    
        