class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        pointerA = 0
        pointerB = 0
        
        while(pointerA <= len(s) - 1 and pointerB <= len(t) - 1):
            
            checkChar = s[pointerA]
            
            if checkChar == t[pointerB]:
                pointerA +=1
            
            pointerB +=1
        
        if pointerA > len(s) - 1:
            return True
        
        return False