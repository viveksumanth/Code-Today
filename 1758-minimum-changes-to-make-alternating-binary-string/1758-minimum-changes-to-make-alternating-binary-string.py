class Solution:
    def minOperations(self, s: str) -> int:
        cB = False
        startZeroCount = 0
        startOneCount = 0
        
        for i in range(0, len(s)):
            if cB == False:
                if s[i] != '0':
                    startZeroCount += 1
                cB = True
                
            elif cB == True:
                if s[i] != '1':
                    startZeroCount += 1
                cB = False
                    
        cB = False
        for i in range(0, len(s)):
            if cB == False:
                if s[i] != '1':
                    startOneCount += 1
                cB = True
            
            elif cB == True:
                if s[i] != '0':
                    startOneCount += 1
                cB = False
        
        return min(startZeroCount, startOneCount)
        
        
                    