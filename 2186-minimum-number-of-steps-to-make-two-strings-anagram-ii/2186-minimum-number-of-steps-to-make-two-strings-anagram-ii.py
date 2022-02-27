from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s = Counter(s)
        t = Counter(t)

        steps = 0
        
        for each in s:
            
            if each in t:
                
                if t[each] > s[each]:
                    steps += t[each] - s[each]

            else:
                
                steps += s[each]


        
        for each in t:
            
            if each in s:
                
                if s[each] > t[each]:
                    steps += s[each] - t[each]

            else:
                
                steps += t[each]

        return steps
        
        