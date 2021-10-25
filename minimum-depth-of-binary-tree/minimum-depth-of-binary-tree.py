# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_children(self,root):
        children = []

        if root.left:
            children.append(root.left)
        if root.right:
            children.append(root.right)
            
        return children

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        depth = 1
        queue = [root]
        
        while(len(queue)):
            
            for i in range(0, len(queue)):
                node = queue.pop(0)
                children = self.get_children(node)
                
                if len(children) == 0:
                    return depth 
                
                for child in children:
                    queue.append(child)
            
            depth+= 1
            
        return depth