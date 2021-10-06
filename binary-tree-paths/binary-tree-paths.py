# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode] ) -> List[str]:
        
        def dfs(root, currentpath, allpaths):
            
            if root.left == None and root.right == None:
                # print(root.val)
                k = ('->'.join(currentpath))
                if len(k) == 0:
                    k = str(root.val)
                else:
                    k = k + '->' + str(root.val)
                allpaths.append(k)
                return allpaths

            if root.left != None:
                dfs(root.left, currentpath + [str(root.val)], allpaths)

            if root.right != None:
                dfs(root.right, currentpath + [str(root.val)], allpaths)
            
            # print(allpaths)
            return allpaths
        
        
        if root:
            return(dfs(root,[],[]))
    
        return []
        
        