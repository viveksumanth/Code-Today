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
    
    def dfs(self, matrix, coordinate, currentPath, memo, visited):
        # print("coordinate: " + str(coordinate))
        # print("memo: " + str(memo))
        if coordinate in memo:
            return memo[coordinate]
        
        neighbours = self.getNeighbours(matrix, coordinate)
        # print("Neighbours of "+ str(coordinate) + " are " + str(neighbours))
        
        if len(neighbours) == 0:
            return currentPath
        tempPath = float("-inf")
        for each in neighbours:
            if each not in visited:
                visited.add(each)
                tempPath = max(tempPath, 
                                       self.dfs(matrix, each, currentPath, memo, visited)+1)
                visited.remove(each)
        memo[coordinate] = tempPath
        return tempPath
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        memo = dict()
        longestPath = 1
        
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix[0])):
                coordinate = tuple([i,j])
                visited = set()
                visited.add(coordinate)
                currentPath = 1
                longestPath = max(longestPath, 
                                  self.dfs(matrix, coordinate, currentPath, memo, visited))
                # print(memo)
                # print("-----------------------")
        return longestPath
    