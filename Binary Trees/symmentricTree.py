class Node:
    
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

tree1 = Node(1)
tree1.left = Node(3)
tree1.right = Node(3)
tree1.right.left = Node(7)
tree1.left.left = Node(7)


'''

check if tree is symmentric


           1                
        /     \          
       3        3             
     /           \           
    7             7        

output = True

                 46
                 / \
                /   \
               /     \
              /       \
             /         \
            /           \
           /             \
          /               \
         /                 \
        85                 91
       / \                 / \
      /   \               /   \
     /     \             /     \
    /       \           /       \
   43       40         8        48
  / \       / \       / \       / \
 /   \     /   \     /   \     /   \
36   40   98   74   98   21   97   59
 
Output: False

'''


class Solution:
    
    def isSymmentricHelper(self, leftTree, rightTree):

        if leftTree == None and rightTree == None:
            return True
        
        elif leftTree == None or rightTree == None:
            return False
        
        elif leftTree.data != rightTree.data:
            return False
        
        return self.isSymmentricHelper(leftTree.left, rightTree.right) and self.isSymmentricHelper(leftTree.right, rightTree.left)


    def isSymmetric(self, root):
        
        if root == None:
            return True

        return self.isSymmentricHelper(root.left, root.right)



answer = Solution()
ans = answer.isSymmetric(tree1)

print(ans)