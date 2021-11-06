'''
        
                leetcode         ["leet","code"]

            leet / \ code
                    x
              code

         leet / \ code
             x    ''

'''
class Solution:
            
        
    def DFS(self, s, wordDict, currentIdx, memo):
        
        currentString = s[currentIdx::]
        
        if currentIdx == len(s):
            return True
        
        if currentString in memo:
            return memo[currentString]

        flag = False
        for word in wordDict:
            
            if currentString.startswith(word): 
                if self.DFS(s, wordDict, currentIdx + len(word), memo):
                    memo[currentString] = True
                    flag = True
                    break
        
        memo[currentString] = flag
        return flag

        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        return self.DFS(s, wordDict, 0, {})

    
        