class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        '''
        ())
        
        {( : )}
        
        []
        )
        
        we encounter a closing bracket and we have out stack empty which means we need to add it
        
        ()))((  -> ((()))(())
        
        [))]
        
        minadd =         
        
        by the end of the string if they are still elements in the stack which means that we have to add them  to make our string valid
        
        '''
        
        lookup = {'(':')'}
        closingBracket = ')'
        stack = []
        minmAdd = 0
        
        for idx in range(0,len(s)):
            if s[idx] in lookup:
                stack.append(lookup[s[idx]])
            
            elif s[idx] == closingBracket:
                
                if len(stack) == 0:
                    minmAdd += 1
                else:
                    stack.pop()
        
        if len(stack):
            minmAdd += len(stack)
        
        return minmAdd
        
        