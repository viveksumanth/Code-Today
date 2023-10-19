# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def moveLeft(self, root):
        leftNodes = []
        while(root != None):
            leftNodes.append(root)
            root = root.left
        return leftNodes
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        
        stack = self.moveLeft(root)
        while(stack):
            # append stack untill the left is not none
            currentNode = stack.pop()
            result.append(currentNode.val)
            if currentNode.right:
                rightNode = currentNode.right
                stack.append(rightNode)
                getLeftNodes = self.moveLeft(rightNode.left)
                stack.extend(getLeftNodes)
        
        return result
            
            