# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.countNodes = 0
        
    def dfs(self,root,maxSoFar):
        if root == None:
            return 
        
        if root.val >= maxSoFar:
            self.countNodes += 1
        
        self.dfs(root.left, max(maxSoFar, root.val))
        self.dfs(root.right, max(maxSoFar, root.val))
        
        return
            
    def goodNodes(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        maxSoFar = root.val
        
        self.dfs(root,maxSoFar)
        return self.countNodes
        