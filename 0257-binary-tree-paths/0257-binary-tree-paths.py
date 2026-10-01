# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    
    def binaryTreePaths(self, root: TreeNode | None, currentResult='') -> list[str]:
        if root.left == None and root.right == None:
            self.result.append(currentResult + str(root.val))
            return self.result
        
        currentResult = currentResult + str(root.val) + '->'
        for each in [root.left, root.right]:
            if each != None: 
                self.binaryTreePaths(each, currentResult)
        
        return self.result
