class Solution:
    def numDecodings(self, s: str) -> int:
        
        letterlist = [str(i) for i in range(1,27)]
        memo = {}
        
        def dfs(start):

            if start == len(s):
                return 1
            
            if start in memo:
                return memo[start]
            
            remaining = s[start::]
            ways = 0
            
            for each in letterlist:
                if remaining.startswith(each):
                    ways += dfs(start+len(each))
                    memo[start] = ways
            
            return ways
        
        return dfs(0)
        
        
        
                