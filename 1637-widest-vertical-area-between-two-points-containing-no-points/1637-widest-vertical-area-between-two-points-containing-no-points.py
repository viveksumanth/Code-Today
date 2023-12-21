class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        result = 0
        for each in range(1, len(points)):
            diff = points[each][0] - points[each-1][0]
            result = max(result, diff)
        
        return result
            