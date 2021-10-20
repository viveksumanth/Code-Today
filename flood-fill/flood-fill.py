class Solution:
    
    def get_neighbours(self,rows,cols,curr_row,curr_col):
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        neighbours = []
        
        for i in range(4):
            neighbour_row = curr_row + delta_row[i]
            neighbour_col = curr_col + delta_col[i]
            
            if ((0 <= neighbour_row < rows and 0 <= neighbour_col < cols)):
                neighbours.append([neighbour_row, neighbour_col])
        
        return neighbours
            
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        number_of_rows = len(image)
        number_of_cols = len(image[0])
        queue = [[sr,sc]]
        old_color = image[sr][sc]
        image[sr][sc] = newColor
        visited = []
        
        while(len(queue)):
            node = queue.pop()
            
            for i in self.get_neighbours(number_of_rows,number_of_cols,node[0],node[1]):
                # print(i[0],i[1])
                if i not in visited and image[i[0]][i[1]] == old_color:
                    visited.append(i)
                    queue.append([i[0],i[1]])
                    image[i[0]][i[1]] = newColor
        
        return image
                    
                    
                    
        
        
        
        