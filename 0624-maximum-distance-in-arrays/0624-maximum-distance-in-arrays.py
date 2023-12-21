class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        gMaxElement = arrays[0][-1]
        gMinElement = arrays[0][0]
        gres = 0
        size = len(arrays)
        
        for i in range(1, len(arrays)):
            cMinElement = arrays[i][0]
            cMaxElement = arrays[i][-1]
            
            currDiff1 = abs(cMaxElement - gMinElement)
            currDiff2 = abs(gMaxElement - cMinElement)
            
            cres = max(currDiff1, currDiff2)
            gres = max(gres, cres)
            
            gMinElement = min(gMinElement, cMinElement)
            gMaxElement = max(gMaxElement, cMaxElement)
            
        return gres
    