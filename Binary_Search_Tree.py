class Node:
    """A node in the binary search tree."""
    def __init__(self, key: int):
        self.key = key
        self.left: Node | None = None   # subtree of smaller keys
        self.right: Node | None = None  # subtree of larger keys

class BinarySearchTree:
    """Simple BST with insert, search, and in-order traversal."""
    def __init__(self):
        self.root: Node | None = None

    def insert(self, key: int) -> None:
        """Insert `key` into the BST."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node: Node | None, key: int) -> Node:
        if node is None:
            # Found the spot: create a new node
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        # if key == node.key: ignore duplicates (or handle as you wish)
        return node

    def search(self, key: int) -> bool:
        """Return True if `key` is in the BST."""
        return self._search_recursive(self.root, key) is not None

    def _search_recursive(self, node: Node | None, key: int) -> Node | None:
        if node is None:
            # Reached a leaf—key not found
            return None
        if key == node.key:
            # Key found
            return node
        # Recurse into the side where the key could be
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder(self) -> list[int]:
        """Return a sorted list of all keys via in-order traversal."""
        result: list[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Node | None, result: list[int]) -> None:
        if node is not None:
            # Visit left subtree, then node, then right subtree
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    # Example usage
    bst = BinarySearchTree()
    for value in [7, 3, 9, 1, 5]:
        bst.insert(value)

    print("In-order traversal:", bst.inorder())  # [1, 3, 5, 7, 9]
    print("Search for 5:", bst.search(5))        # True
    print("Search for 8:", bst.search(8))        # False