# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.treeArray = []
        
    def makeTree(self,left,right,root):
        
        '''
        recursiverly placing the middle element into Tree
        
        [1,2,3,4]
        
        '''
        if left > right:
            return 
        
        midIdx = (left + right)//2
        midNode = self.treeArray[midIdx]
        
        root = TreeNode(midNode)
        root.left = self.makeTree(left,midIdx-1,root)
        root.right = self.makeTree(midIdx+1,right,root)

        return root
            
            
    
    def getInorderTraversal(self,root):
        
        if root == None:
            # self.treeArray.append(None)
            return 
        
        self.getInorderTraversal(root.left)
        self.treeArray.append(root.val)
        self.getInorderTraversal(root.right)
        
        return 
    
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.getInorderTraversal(root)
        self.treeArray.sort()
        newRoot = self.makeTree(0,len(self.treeArray)-1, None)
        return newRoot
        