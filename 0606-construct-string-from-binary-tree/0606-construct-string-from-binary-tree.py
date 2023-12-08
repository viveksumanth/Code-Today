# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, result):
        if root == None:
            return 
        result.append(str(root.val))
        if root.left == None and root.right == None:
            return 
        result.append("(")
        self.dfs(root.left, result)
        result.append(")")
        
        if root and root.right:
            result.append("(")
            self.dfs(root.right, result)
            result.append(")")
        return
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        self.dfs(root, result)
        return ''.join(result)