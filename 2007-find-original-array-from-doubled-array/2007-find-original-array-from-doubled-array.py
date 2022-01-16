from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed)%2 == 1:
            return []
        
        changed.sort()
        result = []
        counter = Counter(changed)
        
        for eachElement in changed:
            
            if eachElement == 0 and counter[eachElement] == 1:
                return []
            
            elif int(eachElement/2) in counter and counter[eachElement/2] > 0:
                
                # print(eachElement/2, eachElement)
                
                counter[int(eachElement/2)] -= 1
                counter[eachElement] -= 1
                result.append(int(eachElement/2))
            
        
        if len(result) != len(changed)//2:
            return []
        return result
        
        