class Solution:
    def generate_neighbours(self,grid, coordinate): #generate all valid states
        row,col = coordinate
        neighbours = []
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        
        for each in range(0,len(delta_row)):
            new_row = row + delta_row[each]
            new_col = col + delta_col[each]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                neighbours.append([new_row,new_col])
        
        return neighbours

    def dfs(self, grid, coordinate):
        neighbours = self.generate_neighbours(grid, coordinate)
        if len(neighbours) == 0:
            return 
        
        for each in neighbours:
            row, col = each
            if grid[row][col] == '1':
                grid[row][col] = '2'
                self.dfs(grid, [row,col])
        
        return 

    def numIslands(self, grid: List[List[str]]) -> int:
        islandsCount = 0
        for row in range(0,len(grid)):
            for col in range(0,len(grid[0])):
                if grid[row][col] == '1':
                    grid[row][col] == '2'
                    islandsCount += 1
                    self.dfs(grid, [row,col])
        
        return islandsCount
        