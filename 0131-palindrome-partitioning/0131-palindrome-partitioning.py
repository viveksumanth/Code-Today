class Solution:
    def __init__(self):
        self.result = []
        self.current = []

    def isParlindrome(self, s: list[str]) -> bool:
        if s == s[::-1]:
            return True
        return False

    def dfs(self, s, idx = 0):
        if idx == len(s):
            self.result.append(self.current[:])
            return 
        
        for i in range(idx, len(s)):
            state = s[idx:i+1]
            if not self.isParlindrome(state):
               continue
            self.current.append(state)
            self.dfs(s, i+1)
            self.current.pop()
        return 
        

    def partition(self, s: str) -> list[list[str]]:
        self.dfs(s, 0)
        return self.result