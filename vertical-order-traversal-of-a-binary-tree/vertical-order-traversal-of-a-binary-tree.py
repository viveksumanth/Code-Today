# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def __init__(self):
        self.verticalOrder = defaultdict(lambda: defaultdict(list))
        
    def generateVerticalNodes(self, root, level, depth):
        if root == None:
            return 
        

        self.verticalOrder[level][depth].append(root.val)
        self.generateVerticalNodes(root.left, level-1, depth+1)
        self.generateVerticalNodes(root.right, level+ 1, depth+1)
        
        return 
        
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        orderResult = []
        
        if root == None:
            return []
        
        self.generateVerticalNodes(root, 0, 0)
    
        # print(self.verticalOrder)
        
        for row in sorted(self.verticalOrder):
            temp = []
            for col in sorted(self.verticalOrder[row]):
                for each in sorted(self.verticalOrder[row][col]):
                    temp.append(each)
            orderResult.append(temp)
            # print(self.verticalOrder[row])
            
        return orderResult
            
        
        
        