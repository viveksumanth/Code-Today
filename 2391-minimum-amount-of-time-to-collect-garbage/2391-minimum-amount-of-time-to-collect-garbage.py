from collections import defaultdict
from collections import Counter

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #make dataset
        '''
        maximumDistance
        {
        G:
        P:
        M: maximumHouse we need to travel to collect this garbage
        }
        
        Amount of Crap
        {
        G:
        P:
        M: 
        }
        '''
        result = 0
        maximumDistance = dict()
        crapAmount = dict()
        distancePrefix = list()
        
        for eachHouse in range(0,len(garbage)):
            for eachCrap in garbage[eachHouse]:
                if eachCrap not in crapAmount:
                    crapAmount[eachCrap] = 0
                crapAmount[eachCrap] += 1
                maximumDistance[eachCrap] = eachHouse
        
        distancePrefix.append(0)
        prevSum = 0
        for each in travel:
            prevSum += each
            distancePrefix.append(prevSum)
        
        for eachCrap in crapAmount:
            result += crapAmount[eachCrap] + distancePrefix[maximumDistance[eachCrap]]

        return result