# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        stack1 = []
        stack2 = []
        result = []
        
        while(True):
            
            # print(stack1)
            # print('and')
            # print(stack2)
            
            while(root1!= None):
                stack1.append(root1)
                root1 = root1.left
            
            while(root2!= None):
                stack2.append(root2)
                root2 = root2.left
                
            if len(stack1) > 0 and len(stack2) > 0:
                
                if stack1[-1].val < stack2[-1].val:
                    node = stack1.pop()
                    result.append(node.val)
                    root1 = node.right

                else:
                    node = stack2.pop()
                    result.append(node.val)
                    root2 = node.right
                    
            elif len(stack1) > 0:
                node = stack1.pop()
                result.append(node.val)
                root1 = node.right
                
            elif len(stack2) > 0:
                node = stack2.pop()
                result.append(node.val)
                root2 = node.right
                
            else:
                break
                
        return result
    
        
        
        