from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hm = Counter(arr)
        
        for i in target:
            if i not in hm:
                return False
            else:
                hm[i] -= 1
                if hm[i] == 0:
                    del hm[i]
        return True
                