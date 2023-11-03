class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        '''
        
        3
        resultStack = ["push", "push", "pop", "push"]
        elements = [1,3]
        pointer = 1
        target = [1,3]
        '''
        resultStack = []
        elements = []
        pointer = 0
        for i in range(1, n+1):
            elements.append(i)
            resultStack.append("Push")
            if elements[-1] != target[pointer]:
                elements.pop()
                resultStack.append("Pop")
                pointer -= 1
            pointer += 1
            
            if elements == target:
                return resultStack
        return resultStack
            
        