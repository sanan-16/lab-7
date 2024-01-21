class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    if root is None:
        return None

    # If either node1 or node2 is the root, the root is the LCA
    if root.key == node1 or root.key == node2:
        return root

    # Recursively search in the left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # If both nodes are found in different subtrees, the current root is the LCA
    if left_lca is not None and right_lca is not None:
        return root

    # If either node is found in one subtree, return that subtree's LCA
    return left_lca if left_lca is not None else right_lca

# Example usage
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

node1 = 5
node2 = 1
lca = find_lca(root, node1, node2)

if lca:
    print(f"The Lowest Common Ancestor of {node1} and {node2} is {lca.key}")
else:
    print(f"At least one of the nodes {node1} or {node2} is not present in the tree.")
