from collections import deque
class Solution:

    def getVacantRooms(self, currentPosition, rooms):
        emptyRoom = 2147483647
        deltaRow = [-1, 0, 1, 0]
        deltaCol = [0, 1, 0, -1]
        cRow, cCol = currentPosition
        vacantRooms = list()
        for i in range(len(deltaCol)):
            newRow = cRow + deltaRow[i]
            newCol = cCol + deltaCol[i]
            if 0 <= newRow < len(rooms) and 0 <= newCol < len(rooms[0]) and rooms[newRow][newCol] == emptyRoom:
                vacantRooms.append([newRow, newCol])
        
        return vacantRooms

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        gatesPosition = []
        # find gates posistion
        for eachRow in range(0,len(rooms)):
            for eachCol in range(0, len(rooms[0])):
                if rooms[eachRow][eachCol] == 0:
                    gatesPosition.append([eachRow, eachCol])
        
        # perform BFS
        queue = deque(gatesPosition)
        nearestGate = 1
        while(len(queue)):
            for i in range(0, len(queue)):
                currentPosition = queue.popleft()
                vacantRooms = self.getVacantRooms(currentPosition, rooms)
                for eachRoom in vacantRooms:
                    row, col = eachRoom
                    rooms[row][col] = nearestGate
                    queue.append(eachRoom)
            nearestGate += 1
        
