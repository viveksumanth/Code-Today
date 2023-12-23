class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinate = [0,0]
        visited = []
        visited.append(coordinate[:])
        
        for each in path:
            if each == 'N':
                coordinate[1] += 1
            elif each == 'S':
                coordinate[1] -= 1
            elif each == 'W':
                coordinate[0] -= 1
            else:
                coordinate[0] += 1

            if coordinate in visited:
                return True
            visited.append(coordinate[:])
        
        
        return False
                
        