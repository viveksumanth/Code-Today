class Solution:
    def generateStates(self,grid,coordinate):
        
        row,col = coordinate
        deltaRow = [-1,-1,-1,0,1,1,1,0]
        deltaCol = [-1,0,1,1,1,0,-1,-1]
        rowLength = len(grid)
        colLength = len(grid[0])
        
        states = []
        
        for idx in range(0,len(deltaRow)):
            
            nRow = deltaRow[idx] + row
            nCol = deltaCol[idx] + col
            
            if 0 <= nRow < rowLength and 0 <= nCol < colLength and grid[nRow][nCol] == 0:
                states.append([nRow,nCol])
        
        return states
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        '''
        
        rows = [-1,-1,-1,0,1,1,1,0]
        cols = [-1,0,1,1,1,0,-1,-1]
        
        '''
        # states = self.generateStates(grid,[0,1])
        # print(states)
        
        start = [0,0]
        end = [len(grid)-1,len(grid[0]) - 1]

        if grid[0][0] != 0:
            return -1
        
        queue = [start]
        distance = 1
        visited = [ [False for i in range(0,len(grid[0]))]  for j in range(0,len(grid))]
        visited[0][0] = True
        
        while(len(queue)):
            

            noNodes = len(queue)
            
            for level in range(0,noNodes):
                
                node = queue.pop(0)
                
                
                if node == end:
                    return distance     
                
                states = self.generateStates(grid,node)
                # print(node,queue,states)
                
                for eachState in states:
                    row,col = eachState
                    if visited[row][col] == False:                       
                        visited[row][col] = True
                        queue.append(eachState)
                        
            distance += 1
        
        return -1
            
        
        
        
        
        