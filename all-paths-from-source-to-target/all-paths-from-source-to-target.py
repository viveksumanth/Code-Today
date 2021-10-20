class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        visited = [False]*len(graph)
        curr = [0]
        start = 0
        target = len(graph) - 1
        
        def dfs(start,result,visited, subpath,target):
            
            if start == target:
                result.append(subpath[:])
            
            for i in graph[start]:
                
                if visited[i] == False:
                    visited[i] = True
                    subpath.append(i)
                    dfs(i, result, visited, subpath, target)
                    subpath.pop()
                    visited[i] = False
            
            return result
        
        return dfs(0, result, visited, curr, target)
        
        
                
        