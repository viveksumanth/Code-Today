# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = []
        inorder = []
        
        while(True):


            
            while(root != None):
                queue.append(root)
                root = root.left
                
            if len(queue) == 0:
               break
            
            node = queue.pop()
            inorder.append(node.val)
            root = node.right
        
        return inorder