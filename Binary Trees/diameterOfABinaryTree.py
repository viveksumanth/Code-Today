class Node:
    
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

tree1 = Node(1)
tree1.left = Node(2)
# tree1.right = Node(3)
# tree1.right.right = Node(7)
tree1.left.left = Node(3)


'''
Find Tree diameter


           1                
        /     \          
       3        3             
     /           \           
    7             7        

output = 5


      5
     /
    5
   / \
  /   \
 /     \
4      10
 \     /
  8   5
 / \   \
8   8   6 
 
Output: 7

'''



class Solution:
    def __init__(self):
        self.maxSoFar = 0
    
    def findDiameter(self,root):
        
        if root == None:
            return 0
        
        left = self.findDiameter(root.left)
        right = self.findDiameter(root.right)

        self.maxSoFar = max(left+right, self.maxSoFar)

        return max(left,right) + 1
        
    def diameter(self,root):
        self.findDiameter(root)
        return self.maxSoFar + 1

answer = Solution()
ans = answer.diameter(tree1)

print(ans)
