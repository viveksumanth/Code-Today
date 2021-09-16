class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph)-1
        stack = [[0]]
        paths = []
        route = [0]
        
        while(stack):
            
            top = stack.pop()
            if top[-1] == target:
                paths.append(top)
            else:
                for each in graph[top[-1]]:
                    stack.append(top + [each])
                    
        return paths