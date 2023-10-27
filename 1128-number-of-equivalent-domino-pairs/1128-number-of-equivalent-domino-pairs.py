from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        sumDict = dict()
        pair = 0
        # for i in range(0, len(dominoes)):
        #     for j in range(i+1, len(dominoes)):
        #         if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]):
        #             pair += 1
        
        listOfTuples = [tuple(sorted(inner_list)) for inner_list in dominoes]
        
        counterList = Counter(listOfTuples)
        
        for each in counterList:
            if counterList[each] > 1:
                pair += math.comb(counterList[each], 2)
                
        return pair
        