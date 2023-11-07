class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for i in range(len(dist)):
            heap.append(dist[i] / speed[i])
            
        heapq.heapify(heap)
        ans = 0
        while heap:
            if heapq.heappop(heap) <= ans:
                break
            
            ans += 1
            
        return ans
        
#         timeToCity = []
        
#         for i in range(0,len(dist)):
#             timeToCity.append(dist[i] // speed[i])
        
#         timeToCity.sort()
#         print(timeToCity)
#         count = 0
        
#         for i in range(1,len(timeToCity)):
#             if timeToCity[i-1] == timeToCity[i]:
#                 return count + 1
#             else:
#                 count += 1
        
#         return count
        