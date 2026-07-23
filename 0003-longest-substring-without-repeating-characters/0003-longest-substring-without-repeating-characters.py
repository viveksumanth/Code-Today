class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointerA = 0
        largestStringLen = 0
        memo = set()

        for pointerB in range(0, len(s)):
            while s[pointerB] in memo:
                memo.remove(s[pointerA])
                pointerA += 1
            
            largestStringLen = max(pointerB-pointerA+1, largestStringLen)
            memo.add(s[pointerB])
        
        return largestStringLen
        

