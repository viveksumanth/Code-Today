class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        timeToCity = []
        
        for i in range(0,len(dist)):
            timeToCity.append(dist[i] / speed[i])
        
        timeToCity.sort()
        count = 0

        for i in range(len(timeToCity)):
            if timeToCity[i] <= i:
                break
            count += 1
            
        return count
        