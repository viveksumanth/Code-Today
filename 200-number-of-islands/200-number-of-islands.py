class Solution:
    def __init__(self):
        self.grid = None
        self.number_of_islands = 0
        
    def generate_neighbours(self,coordinate): #generate all valid states
        row,col = coordinate
        neighbours = []
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        
        for each in range(0,len(delta_row)):
            
            new_row = row + delta_row[each]
            new_col = col + delta_col[each]
            
            if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]) and self.grid[new_row][new_col] == '1':
                neighbours.append([new_row,new_col])
        
        return neighbours
        
    def BFS(self,coordinate):
        
        stack = [coordinate]

        while(len(stack)):
            
            node = stack.pop()
            neighbours = self.generate_neighbours(node)

            for each_neighbour in neighbours:
                row,col = each_neighbour
                self.grid[row][col] = 'V'
                stack.append(each_neighbour)
        
        return
            
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        
        for each_row in range(0,len(self.grid)):
            for each_col in range(0,len(self.grid[0])):
                
                if self.grid[each_row][each_col] == '1':  #island is starting
                    self.number_of_islands += 1
                    self.grid[each_row][each_col] = 'V'
                    self.BFS([each_row,each_col])

        
        return self.number_of_islands
                    