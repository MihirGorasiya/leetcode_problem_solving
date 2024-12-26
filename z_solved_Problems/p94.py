from data_structures.binary_tree import TreeNode

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

res = []


def inorder(root):
    if root:
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
inorder(root)
print(res)