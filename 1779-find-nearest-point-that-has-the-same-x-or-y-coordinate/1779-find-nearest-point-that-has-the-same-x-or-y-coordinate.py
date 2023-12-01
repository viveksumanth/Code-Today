class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        minm = float("inf")
        prevMinm = -1
        for eachPoint in range(0,len(points)):
            pointx, pointy = points[eachPoint]
            if pointx == x or pointy == y:
                distance = abs(x - pointx) + abs(y - pointy)
                minm = min(distance, minm)
                if prevMinm != minm:
                    result = eachPoint
                prevMinm = minm
        
        return result
                
                
        
        
        