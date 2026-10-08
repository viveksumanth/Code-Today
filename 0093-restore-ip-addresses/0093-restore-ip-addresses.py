class Solution:
    def __init__(self):
        self.result = []
        self.current = []
    def dfs(self, s, level, idx):
        if level == 4:
            if idx == len(s):
                ipJoin = '.'.join(self.current)
                self.result.append(ipJoin)
            return
        
        for eachIdx in range(idx, idx+3):
            ipPart = s[idx:eachIdx+1]
            if (len(ipPart) > 1 and ipPart[0] == '0') or (len(ipPart) > 1 and int(ipPart)) > 255:
                continue
            self.current.append(ipPart)
            self.dfs(s, level+1, eachIdx+1)
            self.current.pop()
        return

    def restoreIpAddresses(self, s: str) -> list[str]:
        self.dfs(s, 0, 0)
        return self.result
        