class Solution:
    def getConnectedCells(self, matrix, coordinate):
        row, col = coordinate
        xCoordinates = [-1,0,1,0]
        yCoordiantes = [0,1,0,-1]
        neighbours = []
        
        for i in range(0,len(xCoordinates)):
            newRow = xCoordinates[i] + row
            newCol = yCoordiantes[i] + col
            
            if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]):
                neighbours.append([newRow, newCol])  
        return neighbours

    def dfs(self, coordinate, grid, islandId):
        neighbours = self.getConnectedCells(grid, coordinate)
        if len(neighbours) == 0:
            return 1

        area = 0
        for eachConnectedCell in neighbours:
            row, col = eachConnectedCell
            if grid[row][col] != islandId and grid[row][col] != 0:
                grid[row][col] =  islandId
                area += self.dfs(eachConnectedCell, grid, islandId)
        return area+1

    def findIslands(self, grid, memo) -> None:
        islandId = 2
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = islandId
                    islandArea = self.dfs([row,col], grid, islandId)
                    memo[islandId] = islandArea
                    islandId += 1

    def largestIsland(self, grid: List[List[int]]) -> int:
        memo = dict()
        maxArea = float("-inf")
        self.findIslands(grid, memo)
        
        for rowIdx in range(0,len(grid)):
            for colIdx in range(0,len(grid[0])):
                if grid[rowIdx][colIdx] == 0:
                    currentArea = 1
                    #check surroundings
                    neighbours = self.getConnectedCells(grid, [rowIdx, colIdx])
                    unique = set()
                    for each in neighbours:
                        row, col = each
                        if grid[row][col] != 0:
                            unique.add(grid[row][col])
                    
                    for eachId in unique:
                        currentArea += memo[eachId]

                    maxArea = max(maxArea, currentArea)
        
        if maxArea == float("-inf"):
            for eachId in memo:
                maxArea = max(maxArea, memo[eachId])

        return maxArea