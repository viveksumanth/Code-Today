class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for each in s: 
            if each == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(each)
        return len(stack)