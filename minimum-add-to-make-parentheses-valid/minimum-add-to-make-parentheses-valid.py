class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        store = { ')' : '('}
        stack = [ ]
        
        for i in s:
            
            if i in store and len(stack) and stack[-1] == '(':
                stack.pop()
            
            else:
                
                stack.append(i)
        
        return len(stack)