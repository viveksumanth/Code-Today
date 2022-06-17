class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        
        s = deeedbbcccbdaa
        
        stack = [[a,2]]
        
        
        '''
        
        stack = []
        newString = ''
        for eachChar in s:
            
            if stack and stack[-1][0] == eachChar:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([eachChar,1])
        
        for each in stack:
            newString += each[0]*each[1]
        
        return newString