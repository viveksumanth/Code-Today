class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowLookup = list()
        colLookup = list()
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(0,rows):
            zeroCount = oneCount = 0
            for j in range(0,cols):
                if grid[i][j] == 0:
                    zeroCount += 1
                else:
                    oneCount += 1
            
            rowLookup.append([zeroCount, oneCount])
        
        for i in range(0,cols):
            zeroCount = oneCount = 0
            for j in range(0,rows):
                if grid[j][i] == 0:
                    zeroCount += 1
                else:
                    oneCount += 1
                    
            colLookup.append([zeroCount, oneCount])

        result = [[0 for _ in range(cols)] for _ in range(rows)]
        
        
        for i in range(len(rowLookup)):
            for j in range(len(colLookup)):
                result[i][j] = rowLookup[i][1]  + colLookup[j][1] - rowLookup[i][0] - colLookup[j][0]
        return result
    
    
        