from collections import defaultdict
from collections import Counter

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        houseToGarbageLookup = defaultdict(dict)
        garbageToHouseLookup = defaultdict(set)
        result = 0
        
        #make dataset
        '''
        houseToGarbageLookup ->
        House:{GarbageType:Count}
        {
        0: {g:1}
        1: {p:1}
        2: {g:1,p:2}
        3: {g:2}
        }
        
        garbageToHouseLookup ->
        Garbage:[House]
        {
        g:[0,2,3]
        p:[1,2]
        }
        
        
        '''
        
        for eachHouse in range(0, len(garbage)):
            houseToGarbageLookup[eachHouse] = Counter(garbage[eachHouse])
            for eachCrap in houseToGarbageLookup[eachHouse]:
                    garbageToHouseLookup[eachCrap].add(eachHouse)
        
        for eachCrap in garbageToHouseLookup:
            houseList = garbageToHouseLookup[eachCrap]
            maxHouse = max(houseList)
            distance = sum(travel[0:maxHouse])
            
            for eachHouse in houseList:
                crapCount = houseToGarbageLookup[eachHouse][eachCrap]
                result += crapCount
            result += distance

        return result