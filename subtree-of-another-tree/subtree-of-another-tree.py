# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.isSubTreeInTree = False

    def checkTrees(self, tree, subtree):
        
        if tree == None and subtree != None:
            return False
        
        if subtree == None and tree != None:
            return False
        
        if subtree == None or tree == None:
            return True

        # print(tree.data, subtree.data)
        if tree.val != subtree.val:
            return False
        
        return self.checkTrees(tree.left, subtree.left) and self.checkTrees(tree.right, subtree.right)
        

    def isSubTreeHelper(self, tree, subtree):
        
        # print(tree.data, self.isSubTreeInTree)
        if tree == None:
            return False
        
        if tree.val == subtree.val:

             if self.checkTrees(tree,subtree):
                 self.isSubTreeInTree = True
                 return True

        return self.isSubTreeHelper(tree.left, subtree) or self.isSubTreeHelper(tree.right, subtree)

    def isSubtree(self, tree, subtree):

        self.isSubTreeHelper(tree,subtree)

        return self.isSubTreeInTree