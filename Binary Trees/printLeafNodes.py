class Node:
    
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)


'''
print all leaf nodes

             1
           /  \
          2    3
         / \   / \
        4   5  6  7
'''
class Solution:

    def traversal(self, root):
        
        if root.left == None and root.right == None:
            print(root.val)
            return 

        self.traversal(root.left)
        self.traversal(root.right)
        return 




