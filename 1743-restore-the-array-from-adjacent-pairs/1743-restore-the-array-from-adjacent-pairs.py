from collections import defaultdict
class Solution:
    def restoreArray(self, adjPairs: List[List[int]]) -> List[int]:
        '''
        -2:4
        4:1
        1:-3
        -3:1
        
        * how do you know which one is the first number?
        ** First number and last number appear only once in the adjacent pairs
        
        startNumber = -2
        used = (-2,4)
        -2,4,1,-3
        
        '''
        used = set()
        lookup = defaultdict(list)
        firstDigit = None
        result = []
        
        for eachAdjPair in adjPairs:
            firstNum, secondNum = eachAdjPair
            lookup[firstNum].append(secondNum)
            lookup[secondNum].append(firstNum)
        
        for each in lookup:
            if len(lookup[each]) == 1:
                firstDigit = each
                break

        queue = [firstDigit]
        while(len(queue)):
            currentDigit = queue.pop()
            used.add(currentDigit)
            getnextNode = lookup[currentDigit]
            result.append(currentDigit)
            for eachNode in getnextNode:
                if eachNode not in used:
                    queue.append(eachNode)
        
        return result
        
        