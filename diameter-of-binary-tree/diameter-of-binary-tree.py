# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def recursion(root):
            
            if root == None:
                return 0

            if root:

                ldepth = recursion(root.left)
                rdepth = recursion(root.right)
                print(root.val, ldepth,rdepth)
                
                self.result = max(self.result,rdepth + ldepth)
                return max(ldepth,rdepth) + 1
                
        (recursion(root))
        return self.result
        