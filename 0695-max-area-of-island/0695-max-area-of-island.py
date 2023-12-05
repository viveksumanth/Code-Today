class Solution:
    def getNeighbours(self, matrix, coordinate):
        row, col = coordinate
        xCoordinates = [-1,0,1,0]
        yCoordiantes = [0,1,0,-1]
        neighbours = []
        
        for i in range(0,len(xCoordinates)):
            newRow = xCoordinates[i] + row
            newCol = yCoordiantes[i] + col
            
            if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]):
                if matrix[newRow][newCol] == 1:
                    neighbours.append([newRow, newCol])  
        return neighbours
        
    def dfs(self, grid, coordinate):
        row, col = coordinate
        neighbours = self.getNeighbours(grid, coordinate)
        if len(neighbours) == 0:
            return 1

        currentArea = 0
        for each in neighbours:
            cr,cc = each
            if grid[cr][cc] == 1:
                grid[cr][cc] = 2
                currentArea += (self.dfs(grid, each))
        return currentArea+1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for rowIdx in range(0,len(grid)):
            for colIdx in range(0, len(grid[0])):
                if grid[rowIdx][colIdx] == 1:
                    grid[rowIdx][colIdx] = 2
                    area = self.dfs(grid, [rowIdx, colIdx])
                    maxArea = max(area, maxArea)
        return maxArea