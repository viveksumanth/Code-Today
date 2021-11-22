# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoTree(self,nums,left,right):
        '''
        [-10, -3   0  5, 9]
          0    1   2  3  4
          
          
        '''
        if left > right:
            return
        
        mid = (left + right)//2

        root = TreeNode(nums[mid])
        root.left = self.insertIntoTree(nums, left, mid-1)
        root.right = self.insertIntoTree(nums, mid + 1, right)
        
        return root
        
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        ''' 
                      |
            [-10, -3] 0 [5, 9]
            
            start from the mid of the array 
            
        '''
        if len(nums) == 0:
            return None
        return self.insertIntoTree(nums,0,len(nums)-1)
        
        
        
        