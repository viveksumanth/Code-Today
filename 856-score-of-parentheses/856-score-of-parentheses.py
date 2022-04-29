class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        score = 0

        for each in s:
            if each == '(':
                stack.append(score)
                score = 0
                
            elif each == ')':
                score = stack.pop() + max(2*score,1)
                
        
        return score
    