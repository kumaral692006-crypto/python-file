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

root3=Node(10)
root3.left=Node(5)
root3.right=Node(12)
root3.left.left=Node(3)
root3.left.right=Node(8)
root3.right.right=Node(20)

print("Postorder Traversal(numbers):")
postorder(root3)
print("\n")
