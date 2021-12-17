class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # path = "/a/./b//../../c/"
        path = path.split('/')
        # [a, . , b, /, .. , .. , c ]  

        for idx in range(0,len(path)):

            if path[idx] == '/':
                continue

            elif path[idx] == '.':
                continue

            elif path[idx] == '':
                continue

            elif path[idx] == '..' and stack:
                stack.pop()

            elif path[idx] == '..' and not stack:
                continue

            else:
                stack.append(path[idx])


        absolutePathResult = '/'.join(stack)
        absolutePathResult = '/' + absolutePathResult

        return absolutePathResult
        