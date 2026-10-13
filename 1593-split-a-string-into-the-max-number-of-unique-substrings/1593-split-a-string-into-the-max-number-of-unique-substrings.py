class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        resultSet = set()

        def dfs(s, startIdx, maxLength):
            if startIdx == len(s):
                return len(resultSet)
            
            for eachIdx in range(startIdx, len(s)):
                newSubString = s[startIdx:eachIdx+1]
                if newSubString in resultSet:
                    continue
                
                resultSet.add(newSubString)
                maxLength = max(dfs(s, eachIdx+1, maxLength), maxLength)
                resultSet.remove(newSubString)
            return maxLength
        
        return dfs(s, 0, 0) 