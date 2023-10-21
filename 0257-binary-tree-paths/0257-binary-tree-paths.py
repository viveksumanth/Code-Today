# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getChildren(self, root):
        children = []
        if root == None:
            return children
        
        children.append(root.left) if root.left else None
        children.append(root.right) if root.right else None
        return children
    
    def dfs(self, root, result, currentState):
        if root.left == None and root.right == None:
            resultString = "->".join(currentState[:])
            result.append(resultString)
            return
        
        for eachChild in self.getChildren(root):
            currentState.append(str(eachChild.val))
            self.dfs(eachChild, result, currentState)
            currentState.pop()
        
        return 
            
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root == None:
            return []
        result = []
        self.dfs(root, result, [str(root.val)])
        return result