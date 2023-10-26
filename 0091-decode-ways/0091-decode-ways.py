class Solution:
    def numDecodingHelper(self, s, letters, memo):
        if len(s) == 0:
            return 1
        
        if s in memo:
            return memo[s]
        
        memo[s] = 0
        for i in range(1, len(s)+1):
            if s[:i] in letters:
                memo[s] += self.numDecodingHelper(s[i::], letters, memo)
        return memo[s]

    def numDecodings(self, s: str) -> int:
        letters  = [str(i) for i in range(1,27)]
        memo = {}
        self.numDecodingHelper(s, letters, memo)
        return memo[s]
        