
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        firstDiffIdx = -1
        secondDiffIdx = -1

        for idx in range(0,len(s1)):
            if s1[idx] != s2[idx]:
                if firstDiffIdx == -1:
                    firstDiffIdx = idx
                elif secondDiffIdx == -1:
                    secondDiffIdx = idx
                else:
                    return False

        return s1[firstDiffIdx] == s2[secondDiffIdx] and s1[secondDiffIdx] == s2[firstDiffIdx]


