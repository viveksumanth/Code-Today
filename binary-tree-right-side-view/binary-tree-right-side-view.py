# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateChildren(self,node):
        children = []
        
        if node:
            
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        
        return children
    
        # explores levels
    def levelOrderTraversal(self, root):

      queue = deque()
      queue.append(root)      # [3]
      rightSideView = []      # [1]

      while(len(queue)):

        temp = []
        # moves in the level 
        for level in range(0,len(queue)):

          #current node
          node = queue.popleft()  # 1, 3

          children = self.generateChildren(node)

          temp.append(node.val)   # temp = [3]
          # moves in children
          for child in children:
            queue.append(child)

        rightSideView.append(temp[-1])

      return rightSideView
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
      if root == None:
        return []

      rightSideView = self.levelOrderTraversal(root)

      return rightSideView

        
    
                
        
        
        