class Solution:
    def isValid(self, string: str) -> bool:
        '''
        { '(' : ')', '{' :'}', '[' : ']' }
        
        [({)}]
        
        [ ] ) }]
        
        
        when stack is empty then string is balanced
        
        '''
        
        stack = []
        
        lookup = { '(' : ')', '{' :'}', '[' : ']' }
        
        closingBrackets = ')}]'
        
        for bracket in string:
            
            if bracket in lookup: #check opening bracket and append closing bracket
                
                stack.append(lookup[bracket])
            
            elif bracket in closingBrackets: # check if bracket in closing bracket
                
                # if last element in bracket is not equal to bracket that means we encouterd wrong
                # sequence
                if stack and stack[-1] == bracket:
                    stack.pop()
                else:
                    return False
        
        if len(stack):
            return False
        
        return True