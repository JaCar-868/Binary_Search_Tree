# Binary_Search_Tree
This repository contains a Python implementation of a Binary Search Tree (BST). The BST is a data structure that facilitates fast lookup, addition, and deletion of items. It is structured in a way that each node has at most two children, referred to as the left and right child.

## Features
Insertion: Add new nodes to the BST.
Search: Find nodes in the BST.
Deletion: Remove nodes from the BST.
Traversal: In-order, pre-order, and post-order traversal of the BST.
Minimum and Maximum: Retrieve the minimum and maximum values in the BST.

## File Overview
Binary Search Tree.ipynb: Jupyter Notebook containing the implementation of the BST, along with examples and explanations of each method.

## Getting Started
1. Clone the Repository

git clone https://github.com/your-username/binary-search-tree.git
cd binary-search-tree

2. Installation
Ensure you have Python and Jupyter Notebook installed. If not, you can install them using pip:

pip install notebook

3. Run the Notebook
Launch Jupyter Notebook and open Binary Search Tree.ipynb:

jupyter notebook

## Usage
The Binary Search Tree.ipynb notebook includes detailed explanations and examples of how to use the BST class. Here is a brief overview of the key operations:

1. Insertion

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)

2. Search

node = bst.search(10)
if node:
    print("Node found!")
else:
    print("Node not found!")

3. Deletion
4. 
bst.delete(10)

4. Traversal

bst.in_order_traversal()  # For in-order traversal

5. Minimum and Maximum

min_value = bst.find_min()
max_value = bst.find_max()

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

1. Fork the Repository
2. Create a Branch

git checkout -b feature-branch

3. Commit Your Changes

git commit -m 'Add new feature'

4. Push to the Branch

git push origin feature-branch

5. Open a Pull Request
   
## License
This project is licensed under the MIT License. See the LICENSE file for details.
