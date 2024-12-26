p = [1,2,3], q = [1,2,3]

def isSameTree(node1, node2):
    if not p and not q:
        return True
        # If one is None and the other is not, return False
    if not p or not q:
        return False
        # Check if the current nodes are the same and recurse on children
    return ((p.val == q.val)
            and isSameTree(p.left, q.left)
            and isSameTree(p.right, q.right)
        )