# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True
        
        def checkBalanced(root):
            if root == None:
                return 0

            left_depth = checkBalanced(root.left)
            right_depth = checkBalanced(root.right)

            if abs(left_depth - right_depth) > 1:
                self.balanced = False

            return max(left_depth,right_depth) + 1
        
        checkBalanced(root)
        
        if self.balanced == False:
            return False
        return True
        

        