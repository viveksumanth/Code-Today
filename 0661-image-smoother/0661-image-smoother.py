class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        xCoordinates = [-1,-1,-1,0,1,1,1,0]
        yCoordinates = [-1,0,1,1,1,0,-1,-1]
        colLength = len(img[0])
        rowLength = len(img)
        result = [[0 for i in range(0, colLength)] for j in range(0, rowLength)]
        
        for i in range(0, rowLength):
            for j in range(0, colLength):
                coordinates = []
                
                for k in range(0, len(xCoordinates)):
                    cXCoordinate = xCoordinates[k] + i
                    cYCoordinate = yCoordinates[k] + j
                    
                    if 0 <= cXCoordinate < rowLength and 0 <= cYCoordinate < colLength:
                        coordinates.append([cXCoordinate, cYCoordinate])
                
                currentSum = img[i][j]
                for eachCoordinate in coordinates:
                    row, col = eachCoordinate
                    currentSum += img[row][col]
                    
                result[i][j] = math.floor(currentSum/(len(coordinates)+1))
                
        return result
                    
                    
                    
                    
        
        