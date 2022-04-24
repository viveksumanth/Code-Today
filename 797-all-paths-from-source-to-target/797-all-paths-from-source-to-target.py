class Solution:
    def __init__(self):
        self.target = None
        self.paths = []
        self.graph = None
    
    def dfs(self,current,subpath):
        
        if current == self.target:
            self.paths.append(subpath[:])
            return

        for i in self.graph[current]:
            subpath.append(i)
            self.dfs(i,subpath)
            subpath.pop()
        
        return subpath
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.target = len(graph) - 1
        self.graph = graph
        self.dfs(0,[0])
        return self.paths
        
        
        