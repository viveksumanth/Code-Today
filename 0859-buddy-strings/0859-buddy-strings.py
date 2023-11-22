from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        firstDiff = -1
        secondDiff = -1
        lookup = Counter(s)
        diff = 0

        for idx in range(0,len(s)):
            if s[idx] != goal[idx]:
                if firstDiff == -1:
                    firstDiff = idx
                elif secondDiff == -1:
                    secondDiff = idx
                else:
                    return False
                diff += 1
        
        if diff == 1:
            return False

        if diff == 2:

            # sList = list(s)
            # prev = sList[firstDiff]
            # sList[firstDiff] = sList[secondDiff]
            # sList[secondDiff] = prev
            
            return s[firstDiff] == goal[secondDiff] and s[secondDiff] == goal[firstDiff]

        elif diff == 0:
            for eachChar in lookup:
                if lookup[eachChar] >= 2:
                    return True
        
        return False
        