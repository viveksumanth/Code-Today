class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row = []
        col = []
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
        
        for j in range(0,len(grid[0])):
            for i in range(0,len(grid)):
                if grid[i][j] == 1:
                    col.append(j)
        
        bestMeetingRow = row[len(row)//2]
        bestMeetingCol = col[len(col)//2]
        
        distance = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:

                    distance += abs(bestMeetingRow - i) + abs(bestMeetingCol - j)

        return distance
        