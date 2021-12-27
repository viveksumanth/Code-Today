# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rangeSum = 0
        
    def rangeSumBSTHelper(self,root,low,high):
        
        if root == None:
            return
        
        if low <= root.val and root.val <= high:
            self.rangeSum += root.val
            
        if root.val > low:
            self.rangeSumBSTHelper(root.left,low,high)
        
        if root.val < high:
            self.rangeSumBSTHelper(root.right,low,high)
        
        return

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.rangeSumBSTHelper(root,low,high)
        return self.rangeSum