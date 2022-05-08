
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        
        self.checkInDict = defaultdict()
        self.routeTime = defaultdict(dict)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDict[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInDict[id]
        
        if stationName in self.routeTime[startStation]:
            self.routeTime[startStation][stationName].append(t-startTime)
        else:
            self.routeTime[startStation][stationName] = []
            self.routeTime[startStation][stationName].append(t-startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        alltimes = self.routeTime[startStation][endStation]
        return sum(alltimes)/len(alltimes)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)