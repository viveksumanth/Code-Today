# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.sumOfNodes = 0
    
    def sumOfPathsHelper(self,root,temp):   # 1 [4,9]

        if root == None:
            return
        
        if root.left == None and root.right == None:
            temp += [str(root.val)]
            newValue = int(''.join(temp)) # 491
            self.sumOfNodes += newValue    # 495 + 491 986

        self.sumOfPathsHelper(root.left, temp + [str(root.val)])
        self.sumOfPathsHelper(root.right, temp + [str(root.val)])

        return 

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        self.sumOfPathsHelper(root,[]) #4 []

        return self.sumOfNodes