from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookup = defaultdict(list)
        
        for eachStr in strs:

            sortedLetters = sorted(eachStr)
            sortedStr = ''.join(sortedLetters)
            lookup[sortedStr].append(eachStr)
        
        return lookup.values()
            