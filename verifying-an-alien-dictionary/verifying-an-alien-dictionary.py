class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        lookup = {}
        wordsToNum = []
        for i in range(0,len(order)):
            lookup[order[i]] = i
        
        for word in words:
            temp = []
            for letter in word:
                temp.append(lookup[letter])
            wordsToNum.append(temp)
        
        # print(wordsToNum)
        for i in range(1,len(wordsToNum)):
            if wordsToNum[i-1] > wordsToNum[i]:
                return False
        
        return True 
        
