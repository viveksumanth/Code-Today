# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if root is None:
            return result
        
        stack = [root]
        
        while(stack):
            currentNode = stack.pop()
            result.append(currentNode.val)
            
            if currentNode.right != None:
                stack.append(currentNode.right)
            if currentNode.left != None:
                stack.append(currentNode.left)
        
        return result
    
        