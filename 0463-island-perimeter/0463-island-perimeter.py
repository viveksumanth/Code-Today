class Solution:
    def __init__(self):
        self.grid = None
        self.perimeter = 0
        
    def getLandAndPerimeter(self, currentNode):
        xDirs = [-1,0,1,0]
        yDirs = [0,1,0,-1]
        row, col = currentNode
        perimeter = 0
        land = []
        
        for i in range(0,len(xDirs)):
            nextRow = xDirs[i] + row
            nextCol = yDirs[i] + col
            if 0 <= nextRow < len(self.grid) and 0 <= nextCol < len(self.grid[0]):
                if self.grid[nextRow][nextCol] == 1:
                    land.append([nextRow, nextCol])
                elif self.grid[nextRow][nextCol] == 0:
                    perimeter += 1
            else:
                perimeter += 1
        return [perimeter, land]
    
    def calculatePerimeter(self, currentNode):
        
        row, col = currentNode
        if self.grid[row][col] == 2:
            return 0
        
        self.grid[row][col] = 2
        perimeter, land = self.getLandAndPerimeter(currentNode)
        self.perimeter += perimeter
        for eachLand in land:
            self.calculatePerimeter(eachLand)
        
        return
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        for eachRow in range(0, len(grid)):
            for eachCol in range(0, len(grid[0])):
                if grid[eachRow][eachCol] == 1:
                    self.calculatePerimeter([eachRow, eachCol])
                    return self.perimeter