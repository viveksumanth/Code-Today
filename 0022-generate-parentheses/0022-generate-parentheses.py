class Solution:
    def __init__(self):
        self.result = []
        self.current = []
    
    def dfs(self, n, openCount, closeCount):
        if len(self.current) == n*2:
            self.result.append("".join(self.current))
            return
        
        if openCount > 0:
            self.current.append("(")
            self.dfs(n, openCount-1, closeCount)
            self.current.pop()
        
        if openCount < closeCount:
            self.current.append(")")
            self.dfs(n, openCount, closeCount-1)
            self.current.pop()

        return 

    def generateParenthesis(self, n: int) -> list[str]:
        self.dfs(n, n, n)
        return self.result


            





