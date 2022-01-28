class Node:
    
    def __init__(self,value):
        self.value = value
        self.children = []
    
    def addChild(self,child):
        self.children.append(child)

class Solution:
    def __init__(self):
        self.isLandsCount = 0
        
    def dfs(self,root,prev):

        if root == None:
            return 
        
        for each in root.children:
      
            if prev == 0 and each.value == 1:
                self.isLandsCount += 1

            self.dfs(each,each.value)
            
        return 


    def numberOfIslands(self,root):
    
        if root == None:
            return 0
        
        if root.value == 0:
            self.isLandsCount = 0
        else:
            self.isLandsCount = 1
            
        self.dfs(root,root.value)
        
        print(self.isLandsCount)

    

if __name__ == "__main__":
    # tree = Node(1)                              #[1]
    
    # tree.addChild(Node(0))                  #[0,1,1]
    # tree.addChild(Node(1))
    # tree.addChild(Node(1))
    
    # tree.children[0].addChild(Node(1))       #0 -> [1,0]
    # tree.children[0].addChild(Node(0))
    
    # tree.children[1].addChild(Node(1))      #1 -> [1,1]
    # tree.children[1].addChild(Node(1))
    
    # tree.children[0].children[1].addChild(Node(1))      #
    # tree.children[1].children[1].addChild(Node(0))
    
    # # tree.children[2].addChild(Node(1))
    # # tree.children[3].addChild(Node(1))
    
    # # tree.children[1].children[0].addChild(Node(1))
    
    tree = Node(0)

    tree.addChild(Node(0))
    tree.addChild(Node(1))
    tree.addChild(Node(1))
    
    tree.children[0].addChild(Node(1))
    tree.children[1].addChild(Node(0))
    tree.children[2].addChild(Node(1))
    tree.children[1].children[0].addChild(Node(1))
    
    solution = Solution() 
    solution.numberOfIslands(tree)  