class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        lookup = dict()
        cityA = None
        cityB = None
        for eachPath in paths:
            startCity, nextCity = eachPath
            if startCity not in lookup:
                lookup[startCity] = 1
            else:
                lookup[startCity] += 1
            
            if nextCity not in lookup:
                lookup[nextCity] = 1
            else:
                lookup[nextCity] += 1

        for each in lookup:
            if lookup[each] == 1:
                if cityA == None:
                    cityA = each
                else:
                    cityB = each
                    

        for each in paths:
            if each[0] == cityA:
                return cityB
            elif each[0] == cityB:
                return cityA
        
            
        