
from collections import defaultdict

class Solution:
    
    def nestedString(self,example):
        
        stack = []
        level = 0
        result = defaultdict(list)
        maxLevel = 0
        
        openBrackets = '{[('
        closeBrackets = ')]}'
        
        for eachChar in example:
            if eachChar in openBrackets:
                level += 1
            
            elif eachChar in closeBrackets:
                pointer = len(stack)-1
                currentString = ''
                
                while(stack[pointer] not in openBrackets):
                    currentString += stack.pop()
                    pointer -= 1
                
                stack.pop()
                result[level].append([currentString[::-1]])
                level -= 1
                continue
            
            stack.append(eachChar)
            

        for eachKey in result:
            if eachKey > maxLevel:
                maxLevel = eachKey
        
        if len(stack) == len(example):
            return example
        
        return result[maxLevel]

a = Solution()
print(a.nestedString("[a{{b}c}d(e)]"))
print(a.nestedString("(ab[]c){d{e}}"))
print(a.nestedString("hello! world"))
print(a.nestedString("ab(c(d)e)"))        