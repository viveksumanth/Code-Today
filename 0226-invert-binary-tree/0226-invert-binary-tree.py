# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 
        result = root
        self.invertTreeHelper(root)
        return result
    
    def invertTreeHelper(self, root):
        if root == None:
            return

        tempNode = root.right
        root.right = root.left
        root.left = tempNode

        self.invertTreeHelper(root.left)
        self.invertTreeHelper(root.right)
        return
    

        