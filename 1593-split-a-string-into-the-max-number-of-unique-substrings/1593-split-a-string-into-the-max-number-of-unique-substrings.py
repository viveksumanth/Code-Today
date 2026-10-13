class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        startIdx = 0
        resultSet = []

        def dfs(s, startIdx, maxLength):
            if startIdx == len(s):
                return len(resultSet)
            
            for eachIdx in range(startIdx, len(s)):
                newSubString = s[startIdx:eachIdx+1]
                if newSubString in resultSet:
                    continue
                
                resultSet.append(newSubString)
                maxLength = max(dfs(s, eachIdx+1, maxLength), maxLength)
                resultSet.pop()
            return maxLength
        
        return dfs(s, 0, 0) 