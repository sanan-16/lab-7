class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    else:
        left_count = count_nodes(root.left)
        right_count = count_nodes(root.right)
        return left_count + right_count + 1
