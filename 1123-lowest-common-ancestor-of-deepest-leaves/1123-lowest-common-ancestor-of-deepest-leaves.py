# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root == None:
            return None, 0

        leftAnsestor, lDepth = self.dfs(root.left)
        rightAnsestor, rDepth = self.dfs(root.right)

        if lDepth > rDepth:
            return leftAnsestor, lDepth+1
        elif lDepth < rDepth:
            return rightAnsestor, rDepth+1
        return root, lDepth+1
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        return self.dfs(root)[0]
        