'''
print all paths from source to destination - can move only right and down

source is at [0,0] - 1
destination is at [2,2] - 9

Used BFS to find all paths
Used DFS to print all paths

'''
from collections import defaultdict
import pprint
class PrintAllPaths:
    
    def __init__(self):
        self.pathMap = defaultdict(set)
        self.allPaths = []
        
    def generateChildren(self,node,routeMap):
        row,col = node
        deltaRow = [1,0]
        deltaCol = [0,1]
        neighbours = []
        for each in range(0,len(deltaRow)):
            nRow = row + deltaRow[each]
            nCol = col + deltaCol[each]
            if 0 <= nRow < len(routeMap) and 0 <= nCol < len(routeMap[0]):
                neighbours.append((nRow,nCol))
        
        return neighbours
    
    # dfs to print all paths
    def makePaths(self,start,tempPath):
        
        if self.pathMap[start] == None:
            self.allPaths.append(tempPath[:])
            return 
        
        for each in self.pathMap[start]:
            tempPath.append(each)
            self.makePaths(each,tempPath)
            tempPath.pop()
            
        return
        
    def solution(self,routeMap,source,destination):
        
        self.pathMap[source] = None
        
        #BFS
        queue = [(0,0)]
        seen = set()
        while(len(queue)):
            
            for each in range(len(queue)):
                node = queue.pop(0)
                value = routeMap[node[0]][node[1]]
                neighbours = self.generateChildren(node,routeMap)
                
                
                
                for each in neighbours:
                    if each not in seen:
                        queue.append(each)
                        seen.add(each)
                    row,col = each
                    child = routeMap[row][col]
                    self.pathMap[child].add(value)
        

        self.makePaths(destination,[destination])

        return self.allPaths
        
        

if __name__ == "__main__":
    
    routeMap = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ]
        
    source = 1
    destination = 9
       
    sol = PrintAllPaths()
    allPaths = sol.solution(routeMap,source,destination)
    pprint.pprint(allPaths)