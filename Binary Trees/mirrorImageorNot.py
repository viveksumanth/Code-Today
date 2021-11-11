class Node:
    
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)
tree1.right.right = Node(7)
tree1.right.left = Node(6)

tree2 = Node(1)
tree2.left = Node(3)
tree2.right = Node(2)
tree2.left.left = Node(7)
tree2.left.right = Node(6)

'''
check if two trees are mirror image or not


           1                         1
        /     \                   /    \
       2       3                 3       2
              /   \            /   \     
             6     7          7     6 

output = True


           1                        1
        /     \                  /     \
       2       3                2       3
     /   \   /   \            /   \    / 
    4     5 6     7          4     5  6
 
Output: False

'''
class Solution:

    def traversal(self, tree1, tree2):

        if tree1 == None and tree2 == None:
            return True

        elif tree1 == None or tree2 == None:
            return False

        if tree1.val != tree2.val:
            return False
        

        return self.traversal(tree1.left, tree2.right) and self.traversal(tree1.right, tree2.left)




answer = Solution()
answer.traversal(tree1, tree2)