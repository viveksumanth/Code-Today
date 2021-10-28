# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
        
                1
               / \  
             2     3
            /    /  \
           4    5    6 
          / \
         8   9
             /           
            7
           / 
         11
         /
       13
       /
     14
     
'''
class Solution:

    def __init__(self):
        
        self.maxm = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxm = max(self.maxm, left+right)
            
            return max(left,right)+ 1

        dfs(root)
        return self.maxm 

    