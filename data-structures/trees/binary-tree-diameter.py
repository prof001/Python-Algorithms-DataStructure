class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def diameter_of_binary_tree(root):
    if root is None:
        return 0
    else:
        return sum(_diameter_binary_rec(root))

def _diameter_binary_rec(root):
    node = root
    left_depth = 0
    right_depth = 0

    if root is None:
        return 0

    if node.left is not None:
        left_depth = max(_diameter_binary_rec(node.left))

    if node.right is not None:
        right_depth = max(_diameter_binary_rec(node.right))

    return [left_depth, right_depth]
