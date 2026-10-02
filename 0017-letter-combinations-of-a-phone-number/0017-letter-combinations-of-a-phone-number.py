class Solution:
    def __init__(self):
        self.lookup = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.curResult = []
        self.result = []

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) != 0:
            self.dfs(digits)
        return self.result
    
    def dfs(self, digits, level=0):
        if  len(self.curResult) == len(digits):
            resultString = ''.join(self.curResult)
            self.result.append(resultString)
            return
        
        for each in digits[level]:
            for eachLetter in self.lookup[each]:
                level += 1
                self.curResult.append(eachLetter)
                self.dfs(digits, level)
                self.curResult.pop()
                level -= 1
        return

                
            

        