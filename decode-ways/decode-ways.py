class Solution:
    
    def dfs(self,letterList, memo, s, idx):
        
        current = s[idx::]

        if idx == len(s):
            return 1
        
        if current in memo:
            return memo[current]
        
        total = 0
        for number in letterList:
            if current.startswith(number):
                total +=  self.dfs(letterList, memo, s, idx+len(number))
                memo[current] = total
                
        return total
                
    def numDecodings(self, s: str) -> int:
        
        letterList = [str(i) for i in range(1,27)]
        memo = {}
        return self.dfs(letterList, memo, s, 0)
        
        
        
        
        
        
                