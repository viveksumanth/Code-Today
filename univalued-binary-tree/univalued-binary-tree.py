# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isUnivalTreeHelper(self, root, commonValue):
        
        if root == None:
            return True
        
        if root.val != commonValue:
            return False
        
        return self.isUnivalTreeHelper(root.left,commonValue) and self.isUnivalTreeHelper(root.right, commonValue)
            
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        commonValue = root.val
        
        return self.isUnivalTreeHelper(root, commonValue)
        