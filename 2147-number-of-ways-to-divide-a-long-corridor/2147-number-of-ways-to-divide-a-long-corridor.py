class Solution:
    def __init__(self):
        self.result = 1
        self.MOD = (10**9)+7
    
    def numberOfWays(self, corridor: str) -> int:
        sCount = 0
        for i in range(0,len(corridor)):
            if corridor[i] == "S":
                sCount += 1
        
        if sCount == 0 or sCount%2 != 0:
            return 0
        
        cSCount = 0
        pCount = 1
        
        for i in range(0, len(corridor)):
            if corridor[i] == 'S':
                cSCount += 1
            if cSCount >= 2 and corridor[i] == "P":
                pCount += 1
            if cSCount == 3:
                self.result *= pCount
                cSCount = 1
                pCount = 1
                
        return self.result % self.MOD
        