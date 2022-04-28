class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = list()
        total= 0
        for each in costs:
            a,b = each
            diff.append([[a-b],a,b])
        
        diff.sort()

        for each in range(0,len(diff)//2):
            total += diff[each][1]
        
        for each in range(len(diff)//2,len(diff)):
            total += diff[each][2]
        
        return total
            
        
        
        
        