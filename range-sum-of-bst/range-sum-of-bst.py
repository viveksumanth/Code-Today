# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    do inorder traversal Left Root Right and find the low when low is found we start adding untill we 
    find the high.
    inorder traversal going from left to right gives numbers in ascending order
    
    why shouldn't I pass in a function why should I do globally?
    
    '''
    
    def __init__(self):
        self.currentSum = 0
        self.flag = False

    def rangeSumBSTHelper(self, root, low, high):
        
        
        if root == None:
            return
        
        self.rangeSumBSTHelper(root.left, low, high)
        
        if self.flag == True:
            self.currentSum += root.val
            
        if root.val == low:
            self.flag = True
            self.currentSum = root.val
        
        if root.val == high:
            self.flag = False
            return 

        self.rangeSumBSTHelper(root.right, low, high)
        
        return 

            
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.rangeSumBSTHelper(root, low, high)
        return self.currentSum
    