class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        charecters = set(s)
        result = 0
        for eachChar in charecters:
            leftIndex = s.index(eachChar)
            rightIndex = s.rindex(eachChar)
            seen = set()
            
            for i in range(leftIndex+1, rightIndex):
                seen.add(s[i])
            
            result += len(seen)
            
        return result
        