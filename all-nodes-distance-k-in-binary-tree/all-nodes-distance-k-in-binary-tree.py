# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def __init__(self):
        self.result = []
        self.graph = defaultdict(list)
        self.targetFound = False
    
    def makeGraph(self, root, prev):
        
        if root == None:
            return
        
        if root.left != None:
            self.graph[root.val].append(root.left.val)
        
        if root.right != None:
            self.graph[root.val].append(root.right.val)
        
        if prev != None:
            self.graph[root.val].append(prev.val)
        
        prev = root
        self.makeGraph(root.left,prev)
        self.makeGraph(root.right,prev)
        
        return 
            
    def generateChildren(self,node):

        return self.graph[node]
        
    def findNodesAtDistanceK(self,target,k):
        
        queue = [target.val]
        currentLevel = 0
        visited = set()
        visited.add(target.val)
        
        while(len(queue)):
            
            for level in range(0,len(queue)):
                # print(currentLevel,queue)
                node = queue.pop(0)
                
                children = self.generateChildren(node)
                
                
                for eachChild in children :
                    if eachChild not in visited:
                        visited.add(eachChild)
                        queue.append(eachChild)
                
                # print(currentLevel,queue)
                
                if currentLevel == k:
                    self.result.append(node)
                    
            currentLevel = currentLevel + 1
            
                
                    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        self.makeGraph(root,None)
        
        self.findNodesAtDistanceK(target,k)
        print(self.result)
        return self.result
        