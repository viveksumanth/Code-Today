'''

this is not the code for sourcenode to every other node

this is code to find shortest path from source to destination 

code gives the shortest distance and shortest path.

'''
import heapq

def generateNeighbours(graph,currentNode):
    distance,node= currentNode
    return graph[node]

def generatePath(destination,parent):
    path = []
    currentNode = destination

    while(currentNode != None):
        path.append(currentNode)
        currentNode = parent[currentNode]
        
    return path[::-1]


def findDistanceAndPath(source,destination,graph):
    
    minDistanes = []
    parent = dict()
    parent[source] = None
    source = [0,source]
    heapq.heappush(minDistanes,source)
    visited = set()
    
    while(len(minDistanes)):
        
        currentNode = heapq.heappop(minDistanes)
        cNval,cNName = currentNode
        visited.add(cNName)
        
        if cNName == destination:
            print(cNval)
            return generatePath(destination,parent)

        
        neighbours = generateNeighbours(graph,currentNode)
        
        for eachNeighbour in neighbours:
            node,distance = eachNeighbour
            if node in visited:
                continue
            parent[node] = cNName
            heapq.heappush(minDistanes,[distance+cNval,node])
            
    return -1
    
    
    
if __name__ == "__main__":
    
    source = 'S'
    destination = 'D'
    graph = {
        
        'A':[['B',2],['G',5],['D',11],['S',7]],
        'B':[['C',1],['A',2]],
        'C':[['H',3],['B',1]],
        'H':[['C',3],['D',1],['E',1]],
        'E':[['F',7],['H',1]],
        'F':[['G',2],['E',7],['D',4]],
        'G':[['A',5],['F',2]],
        'D':[['A',11],['F',4],['H',1]],
        'S':[['A',7]]

    }
    
    print(findDistanceAndPath(source,destination,graph))