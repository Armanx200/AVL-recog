class TreeNode: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
class AVL_Tree: 
    def __init__(self):
        self.pre = []
    def insert(self, root, key):  
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 

        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        balance = self.getBalance(root) 
  
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root)
        
        return root 
  
    def leftRotate(self, z): 
        y = z.right 
        T2 = y.left 

        y.left = z 
        z.right = T2 

        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
        return y 
  
    def rightRotate(self, z): 
        y = z.left 
        T3 = y.right 

        y.right = z 
        z.left = T3 

        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
        if not root: 
            return
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left)
        self.preOrder(root.right)

    def preOrdergetlist(self, root): 
        if not root: 
            return
        self.pre.append(root.val)
        self.preOrdergetlist(root.left)
        self.preOrdergetlist(root.right)
    
def isAVL(tree:list):
    myTree = AVL_Tree() 
    root = None
    for node in tree:
        root = myTree.insert(root, node) 
    myTree.preOrdergetlist(root)
    return myTree.pre == tree

        
"""The constructed AVL Tree for [10, 20, 25, 30, 40, 50] would be
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50
"""
print(isAVL([30, 20, 10, 25, 40, 50]))
print(isAVL([30, 20, 25, 10, 40, 50]))
print(isAVL([1]))
