class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for eachElement in s:
            if eachElement == '*':
                if (stack):
                    stack.pop()
            else:
                stack.append(eachElement)
        
        return ''.join(stack)
        