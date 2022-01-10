from collections import defaultdict

class Solution:
    def __init__(self):
        self.path = []
        
    def makeIternary(self,currentPlace,places,routes,visited,airports):
        # print(places)
        if len(places) == airports:
            self.path.append(places[:])
            return True
        
        for idx in range(len(routes[currentPlace])):
            if visited[currentPlace][idx] == False:
                
                nextPlace = routes[currentPlace][idx]
                visited[currentPlace][idx] = True

                places.append(nextPlace)
                ret = self.makeIternary(nextPlace,places,routes,visited,airports)

                visited[currentPlace][idx] = False
                places.pop()
                
                if ret == True:
                    return True
        
        return False
            
            
            
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = defaultdict(list)
        routesVisited = defaultdict(list)
        
        for eachRoute in tickets:
            routes[eachRoute[0]].append(eachRoute[1])
        
        for eachRoute in routes:
            routes[eachRoute].sort()
            routesVisited[eachRoute] = [False]*(len(routes[eachRoute]))
            
        # print(routesVisited)
        self.makeIternary('JFK',['JFK'],routes,routesVisited,len(tickets) + 1)
        
        return self.path[0]
        
        