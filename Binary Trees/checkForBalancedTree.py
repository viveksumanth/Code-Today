class Node:
    
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

tree1 = Node(1)
tree1.left = Node(10)
tree1.right = Node(39)
# tree1.right.right = Node(7)
tree1.left.left = Node(5)


'''
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left 
and right subtrees is not more than one for all nodes of tree.


        1
     /     \
   10      39
  /
5


output = True

        1
     /    
   10   
  /
5
 
Output: False

'''



class Solution:
    def __init__(self):
        self.checkBalanced = True
    
    def isBalancedHelper(self, root):
        if root == None:
            return 0
        
        leftDepth = self.isBalancedHelper(root.left)
        rightDepth = self.isBalancedHelper(root.right)

        if abs(leftDepth - rightDepth) > 1:
            self.checkBalanced = False
    
        return max(leftDepth, rightDepth) + 1

    def isBalanced(self,root):
        
        self.isBalancedHelper(root)

        return self.checkBalanced

solution = Solution()

answer = solution.isBalanced(tree1)

print(answer)