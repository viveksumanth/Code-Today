# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.serializeArray = []
        # self.deserializeArray = []
        self.index = 0
        
    def serializeHelper(self,root):
        if root == None:
            self.serializeArray.append('None')
            return
        
    
        self.serializeArray.append(str(root.val))
        self.serializeHelper(root.left)
        self.serializeHelper(root.right)
        
        return 
        
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        self.serializeHelper(root)
        serializedString = ','.join(self.serializeArray)
        return serializedString
        
    
    def deserializeHelper(self,data, root):
        
        if self.index >= len(data) - 1 or  data[self.index] == 'None':
            self.index += 1
            return
        
        root = TreeNode(data[self.index])
        self.index += 1
        root.left = self.deserializeHelper(data, root)
        root.right = self.deserializeHelper(data, root)
        
        return root
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        deserializedTree = self.deserializeHelper(data,None)
        # print(deserializedTree)
        return deserializedTree
        
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))