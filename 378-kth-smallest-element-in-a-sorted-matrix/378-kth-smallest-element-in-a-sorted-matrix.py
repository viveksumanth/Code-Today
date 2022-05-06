import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        sortedHeap = []
        
        for eachRow in range(0,len(matrix)):
            for eachCol in range(0,len(matrix[0])):
                element = matrix[eachRow][eachCol]
                heapq.heappush(sortedHeap,element)
        
        while(k-1 and len(sortedHeap)):
            heapq.heappop(sortedHeap)
            k = k -1
        
        return heapq.heappop(sortedHeap)
            