
class Node:

    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.left.left = Node(9)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.left.right = Node(7)

'''
print all nodes with single child

             1
           /  \
          2    3
         / \   / 
        4   5  6 
       /        \
      9          7 

output = 4, 3, 6


        1
       /
      2
       \
        3

output 2, 3  
'''
class Solution:

    def traversal(self, root):
        
        if root == None:
            return

        if root.left == None and root.right:
            print(root.val)

        if root.right == None and root.left:
            print(root.val)

        self.traversal(root.left)
        self.traversal(root.right)
        return 



answer = Solution()
answer.traversal(node)