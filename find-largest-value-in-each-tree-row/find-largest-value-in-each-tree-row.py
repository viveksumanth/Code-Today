# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def generateChildren(self, root):
        children = []
        
        if root:
            
            if root.left:
                children.append(root.left)
            if root.right:
                children.append(root.right)
        
        return children
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        BFS and queue
        [1]
        [] 1
        
        '''
        if root == None:
            return []
        
        queue = [root]
        maxArray = []
        
        while(len(queue)):
            
            maxSoFar = float('-inf')
            
            for level in range(0,len(queue)):
                
                node = queue.pop(0)
                
                children = self.generateChildren(node)
                
                for child in children:
                    
                    queue.append(child)
                    
                maxSoFar = max(maxSoFar, node.val)
                
            maxArray.append(maxSoFar)
                    
        
        return maxArray
                    
        