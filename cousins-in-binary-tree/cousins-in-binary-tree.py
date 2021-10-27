# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # use parent as a state
        # when target is found return parent and level
        
        def findcousins(tree, parent, level, find):
            
            if tree == None:
                return 
            
            if tree.val == find:
                return level, parent
            
            return findcousins(tree.left, tree, level+1, find) or findcousins(tree.right, tree, level+1, find)
        
        levelx, parentx = findcousins(root, 0, 0, x )
        levely, parenty = findcousins(root, 0, 0, y )
        
        
        if levelx == levely and parentx != parenty:
            return True
        return False