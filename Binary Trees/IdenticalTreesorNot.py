
class Node:

    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)
tree1.left.left = Node(4)
tree1.left.left.left = Node(7)
tree1.left.right = Node(5)
tree1.right.left = Node(6)
tree1.right.left.right = Node(7)

tree2 = Node(1)
tree2.left = Node(2)
tree2.right = Node(3)
tree2.left.left = Node(4)
tree2.left.left.left = Node(9)
tree2.left.right = Node(5)
tree2.right.left = Node(6)
tree2.right.left.right = Node(7)

'''
check if two trees are mirror image or not


           1                         1
        /     \                   /    \
       2       3                 3       2
              /   \            /   \     
             6     7          7     6 

output = False


           1                        1
        /     \                  /     \
       2       3                2       3
     /   \   /   \            /   \    / \
    4     5 6     7          4     5  6   7
 
Output: True

'''
class Solution:

    def traversal(self, tree1, tree2):

        if tree1 == None and tree2 == None:
            return True

        elif tree1 == None or tree2 == None:
            return False

        if tree1.val != tree2.val:
            return False
        

        return self.traversal(tree1.left, tree2.left) and self.traversal(tree1.right, tree2.right)
        




answer = Solution()
print(answer.traversal(tree1, tree2))