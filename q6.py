class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if node is None:
        return True

    if not min_value < node.key < max_value:
        return False


    return (is_bst(node.left, min_value, node.key) and
            is_bst(node.right, node.key, max_value))


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = is_bst(root)
print("Is the tree a BST?", result)
