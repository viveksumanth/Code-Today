# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = False
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root == None:
            return self.flag
        
        if root:
            if targetSum == root.val and root.left == None and root.right == None:
                self.flag = True
            self.hasPathSum(root.left, targetSum - root.val)
            self.hasPathSum(root.right, targetSum - root.val)
        
        return self.flag
            
            
            
            
            
        