# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = [root]
        alllevels = []
        
        if root == None:
            return alllevels
        
        while(len(queue)):
            
            level = []
            
            for i in range(0,len(queue)):
                
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                level.append(node.val)
            alllevels.append(level)
                 
                
        return alllevels
                
        