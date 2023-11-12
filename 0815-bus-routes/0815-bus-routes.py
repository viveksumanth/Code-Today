from collections import defaultdict

class Solution:
    def __init__(self):
        self.busRoutes = defaultdict(list)
        
    def makeRoutes(self, routes):
        busNumber = 0
        for eachRouteIdx in range(len(routes)):
            for eachStop in routes[eachRouteIdx]:
                self.busRoutes[eachStop].append(eachRouteIdx)
                
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        self.makeRoutes(routes)
        #BFS
        queue = []
        numBuses = 1
        visited = set()
        for eachRoute in self.busRoutes[source]:
            queue.extend(routes[eachRoute])
            visited.add(eachRoute)
        
        while(len(queue)):
            for i in range(0,len(queue)):
                currentLocation = queue.pop(0)

                if currentLocation == target:
                    return numBuses

                for eachDestination in self.busRoutes[currentLocation]:
                    if eachDestination not in visited:
                        visited.add(eachDestination)
                        queue.extend(routes[eachDestination])
            
            numBuses += 1
                
        return -1
        