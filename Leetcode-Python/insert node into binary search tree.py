class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return self.root
        
        else:
            current_node = self.root
            parent_node  = None
            while current_node:
                if val < current_node.info:
                    parent_node = current_node
                    current_node = current_node.left
                    direction = 'left'
                elif val > current_node.info:
                    parent_node = current_node
                    current_node = current_node.right
                    direction = 'right'
        
        if direction == 'left':
            parent_node.left = new_node
        if direction == 'right':
            parent_node.right = new_node


                
                
            

tree = BinarySearchTree()
