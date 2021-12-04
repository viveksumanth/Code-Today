






































































































































































































































































# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def __init__(self):
        self.maxLeft = dict()
        self.maxWidth = 1
        
    
    def maxWidthHelper(self,root,level,posistion,dirn):
        
        if root == None:
            return 

        if level not in self.maxLeft:
            self.maxLeft[level] = posistion

        self.maxWidth = max(posistion - self.maxLeft[level] + 1, self.maxWidth)


        self.maxWidthHelper(root.left,level+1,posistion*2,"left")
        self.maxWidthHelper(root.right,level+1,(posistion*2)+1,"right")
        
        return
        
        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        - when it is a left node then 2*i
        - when it is a right node then 2*i + 1
        
        maintaining a maxleftarray
        
        '''
        # print(self.maxWidth)
        if root == None:
            return None
         
       
        self.maxWidthHelper(root,0,1,None)
        # print(self.maxLeft)
        return self.maxWidth