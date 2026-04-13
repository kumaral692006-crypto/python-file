class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        return node(key)
    if key<root.data:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.left,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
root=None
values=[10,5,15,2,7,20]
for v in values:
    root=insert(root,v)
print("inorder traversal(sorted BST()")
inorder(root)