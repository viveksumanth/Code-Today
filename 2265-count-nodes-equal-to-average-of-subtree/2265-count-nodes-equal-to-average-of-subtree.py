# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    
    def dfs(self, root):
        if root == None:
            return [0, 0]
        
        lNodeCount, leftNode = self.dfs(root.left)
        rNodeCount, rightNode = self.dfs(root.right)
        
        nodeCount = lNodeCount + rNodeCount + 1
        sumOfTree = (leftNode + rightNode + root.val)
        average = sumOfTree//nodeCount
        
        if average == root.val:
            self.result += 1

        return [nodeCount, sumOfTree]
        
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result
        