from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        lookup = Counter(s)
        
        for each in range(len(s)):
            char = s[each]
            if lookup[char] == 1:
                return each
        
        return -1
        