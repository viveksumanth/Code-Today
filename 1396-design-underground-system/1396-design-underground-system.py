from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict(dict)
        self.AtoB = defaultdict(lambda: defaultdict(list))
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        # self.checkin[id][stationName] = t
        self.checkin[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        for each in self.checkin[id]:
            startTime  = self.checkin[id][1]
            self.AtoB[each][stationName].append([t - startTime])
        
        # print(self.AtoB)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = 0
        numOfPeople = len(self.AtoB[startStation][endStation])
        for eachOne in self.AtoB[startStation][endStation]:
            totalTime += eachOne[0]
        
        return totalTime/numOfPeople
            

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)