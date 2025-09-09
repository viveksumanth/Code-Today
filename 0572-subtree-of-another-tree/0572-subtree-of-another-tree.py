# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isIdentical = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        self.isIdentical = False
        self.isSubTreeHelper(root, subRoot)
        return self.isIdentical
    
    def isSubTreeHelper(self, root, subRoot):
        if root == None:
            return

        if root.val == subRoot.val:
            if self.isTreeIdenticalFinder(root, subRoot):
                self.isIdentical = True
                return

        self.isSubTreeHelper(root.left, subRoot)
        self.isSubTreeHelper(root.right, subRoot)
        return
    
    def isTreeIdenticalFinder(self, root, subRoot):
        if (root == None and subRoot != None):
            return False
        
        if (root != None and subRoot == None):
            return False

        if (root == None and subRoot == None):
            return True
        
        if (root.val != subRoot.val):
            return False


        return (self.isTreeIdenticalFinder(root.left, subRoot.left) and self.isTreeIdenticalFinder(root.right, subRoot.right)) 






    
        