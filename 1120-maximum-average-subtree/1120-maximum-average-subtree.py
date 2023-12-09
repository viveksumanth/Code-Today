# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maximumValue = 0
     
    def dfs(self, root):
        if root == None:
            sumOfNodes = 0
            nodeCount = 0
            return (sumOfNodes, nodeCount)
        
        sumOfNodesLeft, leftNodeCount = self.dfs(root.left)
        sumOfNodesRight, rightNodeCount = self.dfs(root.right)
        
        totalSum = sumOfNodesLeft + sumOfNodesRight + root.val
        totalNodeCount = leftNodeCount + rightNodeCount + 1
        averageValue = totalSum/totalNodeCount
        self.maximumValue = max(self.maximumValue, averageValue)
        
        return (totalSum, totalNodeCount)
    
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        totalSum, nodeCount = self.dfs(root)
        return self.maximumValue

        