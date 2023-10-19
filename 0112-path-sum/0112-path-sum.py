# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumHelper(self, root, targetSum, hasPathSum):
        if root == None:
            return 
        
        if targetSum == root.val and root.left == None and root.right == None:
            hasPathSum[0] = True
            # print(root.val, hasPathSum, targetSum)
            return
            
        self.hasPathSumHelper(root.left, targetSum - root.val, hasPathSum)
        self.hasPathSumHelper(root.right, targetSum - root.val, hasPathSum)
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        hasPathSum = [False]
        if root == None:
            return False
        self.hasPathSumHelper(root, targetSum, hasPathSum)
        return hasPathSum[0]
        
        
        
        