# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelorder(self, root, count):
        if root:
            if root.left == None and root.right == None:
                return count 
            count = max(self.levelorder(root.left,count+1),self.levelorder(root.right,count+1))
        return count
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root:
            count = count + 1
            k = self.levelorder(root,count)
            return k
        else:
            return count