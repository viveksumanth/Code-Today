# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isValidBST(self, root, lmax = float('-inf'), rmax = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None:
            return True
        
        if root.val <= lmax or root.val >= rmax:
            return False
        
        return self.isValidBST(root.left, lmax, root.val) and self.isValidBST(root.right, root.val, rmax)
                
        