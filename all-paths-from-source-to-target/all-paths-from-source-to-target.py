class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        curr = [0]
        start = 0
        target = len(graph) - 1
        
        def dfs(start,result,subpath,target):

            if start == target:
                result.append(subpath[:])
            
            for i in graph[start]:

                subpath.append(i)
                dfs(i, result, subpath, target)
                subpath.pop()

            return result
        
        return dfs(0, result, curr, target)
        
        
                
        