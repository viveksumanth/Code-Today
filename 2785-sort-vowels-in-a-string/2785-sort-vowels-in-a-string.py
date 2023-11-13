class Solution:
    def sortVowels(self, s: str) -> str:
        sList = list(s)
        vowelsInString = list()
        vowels = ("a", "A", "e", "E", "i", "I", "O", "o", "U", "u")
        
        for eachChar in sList:
            if eachChar in vowels:
                vowelsInString.append(eachChar)
        
        vowelsInString.sort()
        curChar = 0
        for eachCharIdx in range(0, len(sList)):
            if sList[eachCharIdx] in vowels:
                sList[eachCharIdx] = vowelsInString[curChar]
                curChar += 1
        
        return "".join(sList)
        
                
        