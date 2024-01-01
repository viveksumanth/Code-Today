class Solution:
    def calculateTime(self, pointA, pointB):
        x1,y1 = pointA
        x2,y2 = pointB
        distance = max(abs(x2-x1), abs(y2-y1))
        return distance
        
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(1, len(points)):
            pointA = points[i-1]
            pointB = points[i]
            time += self.calculateTime(pointA, pointB)

        return time
            