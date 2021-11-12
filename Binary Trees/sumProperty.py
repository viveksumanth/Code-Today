class Node:
    
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

tree1 = Node(1)
tree1.left = Node(10)



'''
Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.

     10
    /
  10 


output = True

       1
     /   \
    4     3
   /  \
  5    N
 
Output: False

'''



class Solution:
    def __init__(self):
        self.isSumPropertyTrue = True

    def isSumPropertyHelper(self,root):

        if root == None:
            return

        if root.left == None and root.right == None:
            return root.val
        
        left = self.isSumPropertyHelper(root.left)
        right = self.isSumPropertyHelper(root.right)

        if left + right != root.val:
            self.isSumPropertyTrue = False
        
        return root.val
    
    def isSumProperty(self,root):
        self.isSumPropertyHelper(root)
        return self.isSumPropertyTrue

solution = Solution()

answer = solution.isSumProperty(tree1)

print(answer)


