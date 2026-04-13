class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

root3=Node(9)
root3.left=Node(4)
root3.right=Node(12)
root3.left.left=Node(2)
root3.left.right=Node(7)
root3.right.right=Node(15)

print("Postorder Traversal(numbers):")
postorder(root3)
print("\n")
