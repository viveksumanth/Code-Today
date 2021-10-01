# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxmdepth = 0
        
    def maxDepth(self, root: Optional[TreeNode],depth = 1) -> int:
        
        # recursively going to the depth of the binary tree 
        # depth variable stores the current depth of the binary tree untill it reaches last leaf
        # maximum depth stores the maximum depth of the binary tree
        if root:
            self.maxmdepth = max(depth,self.maxmdepth)
            self.maxDepth(root.left,depth+1)
            self.maxDepth(root.right,depth+1)
        
        return self.maxmdepth