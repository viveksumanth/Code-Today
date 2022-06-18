class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minmLen = float('inf')
        common = ''
        minLenStr = ''
        for eachString in strs:
            minmLen = min(len(eachString),minmLen)
            if len(eachString) == minmLen:
                minLenStr = eachString
        
        for idx in range(0,minmLen):
            currentCommon = minLenStr[idx]
            for eachString in strs:
                if eachString[idx] != currentCommon:
                    return common
                
            common += currentCommon
        
        return common