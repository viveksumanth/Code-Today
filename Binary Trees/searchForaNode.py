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

Search a node exists in tree or not

             1
           /  \
          2    3
         / \   / 
        4   5  6 
       /        \
      9          7 

target = 5 
output = True


        1
       /
      2
       \
        3

target = 5
output = False

'''

class Solution:

    def traversal(self, root, target):
        
        if root == None:
            return False
        
        if root.val == target:
            return True

        return self.traversal(root.left, target) or self.traversal(root.right, target)



answer = Solution()
print(answer.traversal(node, 5))