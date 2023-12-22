class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0
        
        for each in s:
            if each == "0":
                zeros += 1
            else:
                ones += 1
        
        zerosSeen = 0
        onesSeen = 0
        score = 0
        for each in range(0,len(s)-1):
            if s[each] == "0":
                zerosSeen += 1
            else:
                onesSeen += 1
        
            leftScore = zerosSeen
            rightScore = ones - onesSeen
            score = max(score, leftScore + rightScore)
            
        return score