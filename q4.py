class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def calculate_tree_height(root):
    if root is None:
        return 0
    else:
        left_height = calculate_tree_height(root.left)
        right_height = calculate_tree_height(root.right)
        return max(left_height, right_height) + 1
