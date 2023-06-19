
#Defining the Node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
#printing the tree with its subtrees
    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
#buiding the tree by feeding in the Nodes
def build_product_tree():
    #defining the root
    root = TreeNode("\nElectronics")

    #defining subtree Node
    laptop = TreeNode("\t|___Laptop")
    #adding Nodes to the sub tree
    laptop.add_child(TreeNode("\t\t|___Mac"))
    laptop.add_child(TreeNode("\t\t|___Surface"))
    laptop.add_child(TreeNode("\t\t|___Thinkpad"))

    #defining subtree Node
    cellphone = TreeNode("\t|___Cell Phone")
    #adding Nodes to the sub tree
    cellphone.add_child(TreeNode("\t\t|___iPhone"))
    cellphone.add_child(TreeNode("\t\t|___Google Pixel"))
    cellphone.add_child(TreeNode("\t\t|___Vivo"))

    
    #defining subtree Node
    tv = TreeNode("\t|___TeleVision")
    #adding Nodes to the sub tree
    tv.add_child(TreeNode("\t\t|___Samsung"))
    tv.add_child(TreeNode("\t\t|___LG"))

    #Adding subtrees to the root Node
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    #printing out the tree
    root.print_tree()

if __name__ == '__main__':
    #Running the tree
    build_product_tree()
