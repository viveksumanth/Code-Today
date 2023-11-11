from collections import defaultdict
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = defaultdict(list)
        for eachEdge in edges:
            startNode, destinationNode, weight = eachEdge
            self.edges[startNode].append([destinationNode, weight])  
            
    def addEdge(self, edge: List[int]) -> None:
            startNode, destinationNode, weight = edge
            self.edges[startNode].append([destinationNode, weight])  
    
    #Dijkshtra's Algorithm.
    def shortestPath(self, node1: int, node2: int) -> int:
        minHeap = []
        edgesDistance = [float("inf")]*self.n
        minHeap.append([node1, 0])
        edgesDistance[node1] = 0
        
        while(len(minHeap)):
            currentNode, nodeDistance = heapq.heappop(minHeap)
            
            for eachChild in self.edges[currentNode]:
                newNode, distanceToNewNode = eachChild
                distance = distanceToNewNode + nodeDistance
                
                if distance < edgesDistance[newNode]:
                    edgesDistance[newNode] = distance
                    heapq.heappush(minHeap, [newNode, distance])
        
        if edgesDistance[node2] == float("inf"):
            return -1
            
        return edgesDistance[node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)