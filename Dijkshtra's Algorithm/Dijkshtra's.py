import heapq
def getChildren(node,edges):
    
    children = []
    
    for each in edges[node]:
        node,distance = each
        children.append([distance,node])
    
    return children
    
def dijkstrasAlgorithm(start, edges):

    
    minHeap = []
    
    numberOfEdges = len(edges)
    
    minDistances = [float('inf') for i in range(0,len(edges))]
    
    minHeap.append([0,start])
    
    minDistances[start] = 0
    
    while(len(minHeap)):

        nodeDistance,node = heapq.heappop(minHeap)

        
        children = getChildren(node,edges)

        for eachChild in children:
            distanceToNewNode,newNode = eachChild
            
            distance = distanceToNewNode + nodeDistance
            
            if distance < minDistances[newNode]:
                minDistances[newNode] = distance
                heapq.heappush(minHeap,[distance,newNode])
    
    for eachIdx in range(0,len(minDistances)):
        if minDistances[eachIdx] == float('inf'):
            minDistances[eachIdx] = -1
            
    print(parent)
    return minDistances

if __name__ == "__main__":
    
    start = 0
    
    edges  = [
        [[1,1],[2,4]],
        [[0,1],[2,4],[3,2],[4,7]],
        [[0,4],[1,4],[3,3],[4,5]],
        [[2,3],[4,4],[1,2],[5,6]],
        [[2,5],[3,4],[5,7],[1,7]],
        [[4,7],[3,6]]
        
        ]
    
    print(dijkstrasAlgorithm(start, edges))
        
