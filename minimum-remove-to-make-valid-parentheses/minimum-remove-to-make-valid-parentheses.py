class Solution:
    def minRemoveToMakeValid(self, stringx: str) -> str:
        '''
        hm = { ( : ) } closingbracket = )
        
        "lee(t(c)o)de)"
            | |
        bracketpositions = {(:[]}
        
        
        
        ( : [0, 1]
        
        -> using a default dict to store the posisitions of the opened brackets 
        
        -> conditions:
            -> if you encounter ) and defaultdict[ ( ] is empty 
            which means that we have to remove them because we dont need them
            
            -> if you encounter ) and defaultdict[(] is not empty pop that list
            
        -> at the end of the string check defaultdict[(] all those are extra just we need to remove them
        
        Time Complexity O(n)
        space Complexity O(k) at most n
        
        
        '''

        stack = []
        lookup = '('
        stringx = list(stringx)

        for idx in range(0,len(stringx)):

            if stringx[idx] == ')' and stack:
                stack.pop()

            elif stringx[idx] == ')' and not stack:
                stringx[idx] = ''

            elif stringx[idx] == '(':
                stack.append((idx,'('))

        for idx in range(0,len(stack)):
            changeIndex = stack[idx][0]
            stringx[changeIndex] = ''

        return ''.join(stringx)


            
                    
            