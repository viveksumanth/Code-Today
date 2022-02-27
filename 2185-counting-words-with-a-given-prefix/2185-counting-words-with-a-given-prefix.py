class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        
        for eachWord in words:
            if eachWord.startswith(pref):
                
                count += 1
        
        return count
        
        
        