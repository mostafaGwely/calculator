class binaryTree():
    total = 0
    def __init__(self,root=''):
        self.key = root
        self.left = None
        self.right = None
        binaryTree.total = binaryTree.total + 1
    def insertLift(self,tree=''):
        if self.left == None :
            self.left = binaryTree(tree)
        else:
            temp = binaryTree(tree)
            temp.left = self.left
            self.left = temp
    def insertRight(self,tree=''):
        if self.right == None:
            self.right = binaryTree(tree)
        else:
            temp = binaryTree(tree)
            temp.right = self.right
            self.right = temp
    def setRoot(self,value):
        self.key = value
    def getRoot(self):
        return self.key
    def getLift(self):
        return self.left
    def getRight(self):
        return self.right