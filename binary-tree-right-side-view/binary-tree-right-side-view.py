# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generate_children(self,node):
        children = []
        
        if node:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        
        return children
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        queue = [root]
        rightview = []
        
        while(len(queue)):

            rightview.append(queue[-1].val)
            
            for i in range(0,len(queue)):
                
                node = queue.pop(0)
                
                children = self.generate_children(node)
                
                for child in children:
                    queue.append(child)

        
        return rightview
    
                
        
        
        