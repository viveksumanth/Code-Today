class Solution:
    def __init__(self):
        self.number_of_islands = 0
        self.visited = [[]]
        
    def generateNeighbours(self,grid, coordinate):
        nRows = len(grid)
        nCols = len(grid[0])
        # print(nRows,nCols)
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        neighbours = []
        
        for each in range(4):
            row = coordinate[0] + delta_row[each]
            col = coordinate[1] + delta_col[each]
            
            if 0 <= row < nRows and 0 <= col < nCols:
                neighbours.append([row,col])
        
        return neighbours    
    
    def dfs(self,grid, coordinates):
        
        queue = [coordinates]
        
        while(len(queue)):
            
            node = queue.pop(0)
            neighbours = self.generateNeighbours(grid, node)
            # print(neighbours)
            for neighbour in neighbours:
                # print(neighbour)
                curr_row = neighbour[0]
                curr_col = neighbour[1]
                if grid[curr_row][curr_col] != "0" and self.visited[curr_row][curr_col] == False:
                    self.visited[curr_row][curr_col] = True
                    queue.append(neighbour)

        return 1
                    
              
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nRows = len(grid)
        nCols = len(grid[0])
         
        self.visited = [[False for i in range(0,nCols)] for j in range(0, nRows)]
        
        
        
        for row in range(0,nRows):
            for col in range(0, nCols):
                if grid[row][col] != "0" and self.visited[row][col] == False:
                    coordinate = [row,col]
                    self.visited[coordinate[0]][coordinate[1]] = True
                    self.number_of_islands += self.dfs(grid,coordinate)
                    # print(self.visited)
        
        return self.number_of_islands
                
                    
                    
                    
                    
        