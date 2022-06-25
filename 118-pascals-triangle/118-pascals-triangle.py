class Solution:
    def generate(self, numRow: int) -> List[List[int]]:
        
        result = []
        
        if numRow >= 1:
            result.append([1])
        
        while(numRow != 1):
            current = [1]
            tempCurrent = result[-1]
            for eachIdx in range(1,len(tempCurrent)):
                now = tempCurrent[eachIdx-1] + tempCurrent[eachIdx]
                prev = tempCurrent[eachIdx]
                current.append(now)
            
            current.append(1)
            result.append(current)
            numRow -= 1
        
        return result
            
        