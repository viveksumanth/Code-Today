class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        newword = ''
        for each in s:
            
            if (stack and stack[-1][0] == each):
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                     
            else:
                
                stack.append([each,1])
        
        for each in stack:
            newword += each[0]*each[1]
        
        return newword
                
                
                