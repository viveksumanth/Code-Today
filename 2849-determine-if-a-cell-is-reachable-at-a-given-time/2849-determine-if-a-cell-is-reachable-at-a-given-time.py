class Solution:
    '''
    stop thinking BFS or DFS!!! 
    '''
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:    
        height = abs(sx - fx)
        width = abs(sy - fy)
        moveDiagonally = min(height, width)
        moveStraight = abs(height - width)
        distance = moveDiagonally + moveStraight
        # print(moveDiagonally, moveStraight)
        if distance == 0 and t == 1:
            return False
        if distance <= t:
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#     def getChildren(self, currentPlace, target):
#         currentRow, currentCol = currentPlace
#         targetRow, targetCol = target
#         deltaRow = [-1, -1, -1, 0, 1, 1, 1, 0]
#         deltaCol = [-1, 0, 1, 1, 1, 0, -1, -1]
#         children = []
        
#         for i in range(0, len(deltaCol)):
#             childRow = currentRow + deltaRow[i]
#             childCol = currentCol + deltaCol[i]
#             if 1 <= childRow  and 1 <= childCol:
#                 children.append([childRow, childCol])
#         return children
    
#     def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
#         queue = [[sx,sy]]
#         target = [fx, fy]
#         seconds = 0
#         if queue[0] == target and t == 0:
#             return True
        
#         while(len(queue)):
#             if seconds > t:
#                 return False
#             for eachLevel in range(len(queue)):
#                 currentPlace = queue.pop(0)
#                 if currentPlace == target and seconds <= t and seconds > 0:
#                     return True
#                 for eachChild in self.getChildren(currentPlace, target):
#                     if eachChild not in queue:
#                         queue.append(eachChild)
#             seconds += 1
            
#         return False