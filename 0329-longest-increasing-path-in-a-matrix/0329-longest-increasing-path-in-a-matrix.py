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
                if matrix[newRow][newCol] > matrix[row][col]:
                    neighbours.append(tuple([newRow, newCol]))
                    
        return neighbours
    
    def dfs(self, matrix, coordinate, memo):
        if coordinate in memo:
            return memo[coordinate]
        
        neighbours = self.getNeighbours(matrix, coordinate)
        if len(neighbours) == 0:
            return 1
        
        tempPath = float("-inf")
        for each in neighbours:  
            tempPath = max(tempPath, self.dfs(matrix, each, memo)+1)
        memo[coordinate] = tempPath
        return memo[coordinate]
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        
        memo = dict()
        longestPath = 1
        
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix[0])):
                coordinate = tuple([i,j])
                longestPath = max(longestPath, 
                                  self.dfs(matrix, 
                                           coordinate, 
                                           memo))
        return longestPath
    