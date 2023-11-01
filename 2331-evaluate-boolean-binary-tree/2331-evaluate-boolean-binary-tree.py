# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        leftExpression = self.evaluateTree(root.left)
        rightExpression = self.evaluateTree(root.right)
        
        if root.val == 2:
            return leftExpression or rightExpression
        if root.val == 3:
            return leftExpression and rightExpression
        
        return root.val