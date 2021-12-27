# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.currentNode = root
        self.queue = []

    def inorderTraversal(self):
        while(self.currentNode != None):
            self.queue.append(self.currentNode)
            self.currentNode = self.currentNode.left
        
        node = self.queue.pop()
        self.currentNode = node.right
        return node.val
    
    def next(self) -> int:
        
        return self.inorderTraversal()
        


    def hasNext(self) -> bool:
        
        if self.queue or self.currentNode:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()