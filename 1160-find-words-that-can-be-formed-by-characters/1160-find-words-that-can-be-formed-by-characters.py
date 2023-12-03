from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsLookup = Counter(chars)
        totalSum = 0
        
        for each in words:
            eachCounter = Counter(each)
            wordCheck = True
            for eachLetter in eachCounter:
                if eachLetter not in charsLookup:
                    wordCheck = False
                    break
                elif eachCounter[eachLetter] > charsLookup[eachLetter]:
                    wordCheck = False
                    break

            if wordCheck == True:
                totalSum += len(each)
        
        return totalSum
            
            
                    
                    