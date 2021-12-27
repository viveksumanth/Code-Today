class Solution:
    def trap(self, trap: List[int]) -> int:
        
        maximumToRight = [0] *len(trap)
        maximumToLeft = [0] * len(trap)
        maxmRightWall = 0
        maxmLeftWall = 0
        unitsOfWater = 0

        for idx in range(0,len(trap)):
            maximumToRight[idx] = maxmRightWall
            maxmRightWall = max(maxmRightWall,trap[idx])

        for idx in reversed(range(len(trap))):
            maximumToLeft[idx] = maxmLeftWall
            maxmLeftWall = max(maxmLeftWall,trap[idx])

        for idx in range(0,len(maximumToLeft)):

            currentUnit= min(maximumToRight[idx],maximumToLeft[idx]) - trap[idx]

            if currentUnit > 0:
                unitsOfWater += currentUnit

        return unitsOfWater

        