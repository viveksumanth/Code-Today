from collections import OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        
        hm = OrderedDict()
        result = ''
        for i in range(0,len(s)):
            if s[i] in hm:
                hm[s[i]] = hm[s[i]] + 1
            else:
                hm[s[i]] = 1
        
        hm = dict(sorted(hm.items(), key=lambda item: item[1]))
        
        for i in hm:
            while(hm[i] != 0):
                result = i + result
                hm[i] = hm[i] - 1
        
        return result
        
        