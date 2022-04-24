class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for eachChar in s:
            
            if len(stack) == 0:
                stack.append(eachChar)
            else:
                if stack and stack[-1] != eachChar:
                    stack.append(eachChar)
                else:
                    
                    while(stack and stack[-1] == eachChar):
                        stack.pop()

        
        return ''.join(stack)