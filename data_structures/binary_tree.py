class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":

    def inorder(root):
        if root:
            inorder(root.left)
            print(root.val, end=", ")
            inorder(root.right)

    def preorder(root):
        if root:
            print(root.val, end=", ")
            preorder(root.left)
            preorder(root.right)

    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.val, end=", ")

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("In order Traversal: ")
    inorder(root)
    print("\nPre Order Traversal: ")
    preorder(root)
    print("\nPost Order Traversal: ")
    postorder(root)
