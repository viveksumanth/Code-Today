
def generateNeighbours(graph,currentNode):
    return graph[currentNode]

def generatePath(destination,parent):
    path = []
    currentNode = destination

    while(currentNode != None):
        path.append(currentNode)
        currentNode = parent[currentNode]
        
    return path[::-1]

def findPath(source,destination,graph):
    visited = set()
    parent = dict()
    
    parent[source] = None
    
    distance = 0
    queue = [source]
    visited.add(source)
    
    while(len(queue)):
        
        for level in range(0,len(queue)):
            
            node = queue.pop(0)
            
            if node == destination:

                return generatePath(destination,parent)
                
            neighbours = generateNeighbours(graph,node)
            
            for each in neighbours:
                if each not in visited:
                    parent[each] = node
                    visited.add(each)
                    queue.append(each)
                    
        distance = distance + 1
        
    return -1

def findDistance(source,destination,graph):
    
    visited = set()
    distance = 0
    queue = [source]
    visited.add(source)
    
    while(len(queue)):
        
        for level in range(0,len(queue)):
            
            node = queue.pop(0)
            
            if node == destination:
                return distance
                
            neighbours = generateNeighbours(graph,node)
            # print(neighbours)
            for each in neighbours:
                if each not in visited:
                    visited.add(each)
                    queue.append(each)
                    
        distance = distance + 1
        
    return -1

if __name__ == "__main__":
    
    source = 8
    destination = 0
    graph = {
        0:[1],
        1:[0,2,8,7],
        2:[3],
        3:[2,4],
        4:[3,5,8],
        5:[4,6],
        6:[5,7,8],
        7:[1,6],
        8:[1,4,6]
    }
    
    print(findDistance(source,destination,graph))
    print(findPath(source,destination,graph))