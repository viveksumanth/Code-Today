class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        seen = {}
        def dfs(wordDict, s, i):
            
            if i == len(s):
                return True
            if s[i::] in seen:
                return seen[s[i::]]
            
            flag = False
            
            for eachWord in wordDict:
                if s[i:].startswith(eachWord):
                    
                    answer = dfs(wordDict, s, i+len(eachWord))
    
                    if answer:
                        flag = True
                        break

                
            seen[s[i::]] = flag
                
            return flag
        
        return dfs(wordDict, s, 0)