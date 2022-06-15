from collections import defaultdict
import heapq
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        lookup = defaultdict(list)
        
        for eachNum in nums:
            
            if lookup[eachNum - 1]:
                
                currentOccurence = heapq.heappop(lookup[eachNum-1]) 
                heapq.heappush(lookup[eachNum], currentOccurence + 1)
            
            else:
                heappush(lookup[eachNum],1)
            
        # print(lookup)
        
        for each in lookup:
            if len(lookup[each]) >= 1:
                for j in lookup[each]:
                    # print(j)
                    if j < 3:
                        print(lookup[each])
                        return False
        return True
                
        