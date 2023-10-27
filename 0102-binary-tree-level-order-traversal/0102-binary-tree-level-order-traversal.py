# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getChildren(self, node):
        children = []
        if node == None:
            return children
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)
        return children
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = [root]
        
        if root == None:
            return []
        
        while(queue):
            rowResult = []
            for eachRow in range(0, len(queue)):
                currentNode = queue.pop(0)
                rowResult.append(currentNode.val)
                for eachChild in self.getChildren(currentNode):
                    queue.append(eachChild)
            
            result.append(rowResult)
        
        return result
            