class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList = s.split(" ")
        
        for i in range(len(sList)-1, -1,-1):
            if len(sList[i]) > 0:
                return len(sList[i])
        return 0
            