# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root == None:
            return None
        
        if root.val == val:
            return root

        elif root.val < val:
            result = self.searchBST(root.right, val)
        else:
            result = self.searchBST(root.left, val)

        return result
