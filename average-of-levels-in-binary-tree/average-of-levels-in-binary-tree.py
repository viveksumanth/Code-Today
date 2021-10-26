# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getChildren(self,node):
        result = []
        if node.left:
            result.append(node.left)
        if node.right:
            result.append(node.right)
        return result
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = [root]
        alllevels = []
        
        if root == None:
            return None
        
        while(len(queue)):
            
            level = 0
            levelsum = 0
            for i in range(0,len(queue)): # move along the level 
                
                node = queue.pop(0)
                
                children = self.getChildren(node)
                
                for child in children: # move in the children
                    
                    queue.append(child)
                
                level += 1
                levelsum += node.val
                
                
            alllevels.append(levelsum/level)
                 
        return alllevels
    
        