import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Max Heap Implementation
        distances = []
        result = []
        
        for i1,i2 in points:
            
            distance = -((i2)*i2 + (i1)*i1)
            heapq.heappush(distances,(distance,[i1,i2]))
            if len(distances) > k:
                heapq.heappop(distances)
    
        
        for i in range(len(distances)):
            result.append(distances[i][1])
        
        return result
        
        # Min Heap Implementation
#         distances = []
#         result = []
        
#         for i1,i2 in points:
            
#             distance = (i2)*i2 + (i1)*i1
#             heapq.heappush(distances,(distance,[i1,i2]))
        
#         for i in range(k):
#             popped = heapq.heappop(distances)
#             result.append(popped[1])
        
#         return result
            
        
        
        