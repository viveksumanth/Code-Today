# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict 
  
class Solution:
    def __init__(self):
        self.result = defaultdict(int)
    
    def dfs(self, root):
        if root == None:
            return None
        
        self.result[root.val] += 1
        self.findMode(root.left)
        self.findMode(root.right)
        return 
    
    def findHighRepeatedNode(self):
        maxFreq = max(self.result.values())
        ans = []
        
        for key in self.result:
            if self.result[key] == maxFreq:
                ans.append(key)
        return ans
    
            
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.findHighRepeatedNode()
        