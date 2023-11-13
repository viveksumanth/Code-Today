class Solution:
    def sortVowels(self, s: str) -> str:
        sList = list(s)
        vowelsInString = list()
        vowels = "AEIOUaeiou"
        vowelsLookup = {
            0:"A", 1:"E", 2:"I", 3:"O", 4:"U",5:"a", 6:"e", 7:"i", 8:"o", 9:"u"
        }
        vowelCount = [0]*10
        
        for eachChar in sList:
            if eachChar in vowels:
                index = vowels.index(eachChar)
                vowelCount[index] += 1
                
        pointerA = 0
        for eachCharIdx in range(0, len(sList)):
            if sList[eachCharIdx] in vowels:
                while(pointerA < len(vowelCount)):
                    if vowelCount[pointerA] != 0:
                        charecter = vowelsLookup[pointerA]
                        sList[eachCharIdx] = charecter
                        vowelCount[pointerA] -= 1
                        break
                    pointerA += 1
        
        return "".join(sList)
        
                
        