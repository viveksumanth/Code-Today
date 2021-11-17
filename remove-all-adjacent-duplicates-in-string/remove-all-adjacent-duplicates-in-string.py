class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        '''

        '''
        stack = []          
        pointerA = 0
        
        while(pointerA <= len(s) - 1):
            
            if stack and stack[-1] == s[pointerA]:
                stack.pop()
            else:
                stack.append(s[pointerA])
            
            pointerA += 1

                
        return ''.join(stack)