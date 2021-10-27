# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""


"""
class Solution:
    def getchildren(self,root):
        children = []
        
        if root:
            children.append(root.left)
            children.append(root.right)
        
        return children
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        completeness = False
        '''
        [4,5]
        [none, 7]
        '''
        
        while(len(queue)):
            
            node = queue.pop(0)
            children = self.getchildren(node)
            # if child found after the none which means that tree is not balanced
            # if None found after the none state which means that tree is balanced
            
            for child in children:
                if child != None and completeness == False:
                    queue.append(child)
                    
                elif child == None and completeness == False:
                    # print(child)
                    completeness = True
                    
                elif child != None and completeness == True:
                    # print(child)
                    return False
            
        return True
                
                    
        
        
        