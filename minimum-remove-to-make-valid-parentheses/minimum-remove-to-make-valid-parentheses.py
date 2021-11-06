class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        hm = { ( : ) } closingbracket = )
        
        "lee(t(c)o)de)"
            | |
        bracketpositions = {(:[]}
        
        
        
        ( : [0, 1]
        
        -> using a default dict to store the posisitions of the opened brackets 
        -> conditions:
            -> if you encounter ) and defaultdict[ ( ] is empty which means that we have to remove them because 
            we dont need them
            -> if you encounter ) and defaultdict[(] is not empty pop that list
        -> at the end of the string check defaultdict[(] all those are extra just we need to remove them
        
        Time Complexity O(n)
        space Complexity O(k) at most n
        
        
        '''
        s = list(s)
        lookup = { '(' : []}
        i = 0
        
        while(i <= len(s) - 1):
            
            if s[i] == '(':
                lookup['('].append(i)
                
            elif s[i] == ')':
                
                if len(lookup['(']):
                    lookup['('].pop()
                
                elif len(lookup['(']) == 0:

                    s = s[:i] + s[i+1::]
                    i = i - 1
            
            i = i + 1
        
        if len(lookup['(']):
            for idx in lookup['(']:
                s[idx] = ''
        
        s = ''.join(s)
        return s
            
                    
            