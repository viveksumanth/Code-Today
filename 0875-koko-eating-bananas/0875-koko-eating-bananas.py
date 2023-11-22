import math
class Solution:
    def binarySearch(self, piles, h, maxmTime, minmTime):
        result = minmTime
        while(maxmTime < minmTime):
            k = (minmTime + maxmTime)//2
            timeToEat = self.calculateTimeToEat(piles, k)
            if timeToEat > h:
                maxmTime = k+1
            else:
                minmTime = k
                result = k

        return result
        
    
    def calculateTimeToEat(self, piles, k):
        timeToEat = 0
        for each in piles:
            timeToEat += math.ceil(each/k)
        return timeToEat
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Think brute force to get binary search idea
        '''
        minmTime = maximum number of bananas koko should eat inorder to complete in h hours
        maxmTime = minimum number of bananas koko should eat irrespective to time. 
        '''
        return self.binarySearch(piles, h, maxmTime=1, minmTime=max(piles))