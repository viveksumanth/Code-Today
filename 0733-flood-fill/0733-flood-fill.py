class Solution:
    def getNeighbours(self, sr, sc, image, curColor):
        deltaRow = [-1,0,1,0]
        deltaCol = [0,1,0,-1]
        neighbours = []
        numOfRows = len(image)
        numOfCols = len(image[0])
        
        for i in range(4):
            curRow = sr + deltaRow[i]
            curCol = sc + deltaCol[i]
            if 0 <= curRow < numOfRows and 0 <= curCol < numOfCols and image[curRow][curCol] == curColor:
                neighbours.append([curRow, curCol])
        
        return neighbours
        
    def dfs(self, image, sr, sc, color, curColor, visited):
        image[sr][sc] = color
        visited.append([sr,sc])
        neighbours = self.getNeighbours(sr, sc, image, curColor)
        
        if len(neighbours) == 0:
            return
        
        for eachSr, eachSc in neighbours:
            if [eachSr, eachSc] not in visited:
                self.dfs(image, eachSr, eachSc, color, curColor, visited)
        return 
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image,sr,sc,color, image[sr][sc], [])
        return image
        