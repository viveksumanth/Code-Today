# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    
    def binaryTreePaths(self, root: TreeNode | None, currentResult='') -> list[str]:
        currResult = []
        result = []
        def dfs(root):
            if root.left == None and root.right == None:
                currResult.append(str(root.val))
                result.append('->'.join(currResult))
                return result
        
            currResult.append(str(root.val))
            for each in [root.left, root.right]:
                if each != None: 
                    dfs(each)
                    currResult.pop()
        
            return result
        dfs(root)
        return result

