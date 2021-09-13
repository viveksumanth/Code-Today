class Solution:
    def isValid(self, string: str) -> bool:
        hm = {'[':']', '{':'}', '(':')'}
        stack = []
        allbrackets = '{[()]}'
        for i in range(len(string)):

            if string[i] not in stack and string[i] in hm.keys():
                stack.append(hm[string[i]])
            elif string[i] in stack:
                if stack[-1] == string[i]:
                    stack.pop(-1)
                else:
                    return False
            elif string[i] not in hm.keys() and string[i] in allbrackets:
                return False

        if len(stack) == 0:
            return True
        return False
        