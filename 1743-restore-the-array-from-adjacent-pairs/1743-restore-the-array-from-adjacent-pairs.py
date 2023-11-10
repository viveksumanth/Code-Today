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
        count = dict()
        firstDigit = None
        lastDigit = None
        
        for eachAdjPair in adjPairs:
            firstNum, secondNum = eachAdjPair
            if firstNum not in count:
                count[firstNum] = 1
            else:
                count[firstNum] += 1
            
            if secondNum not in count:
                count[secondNum] = 1
            else:
                count[secondNum] += 1
            
            lookup[firstNum].append(secondNum)
            lookup[secondNum].append(firstNum)
        
        for eachNum in count:
            if count[eachNum] == 1:
                if firstDigit == None:
                    firstDigit = eachNum
                else:
                    lastDigit = eachNum
        
        result = []
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
        
        