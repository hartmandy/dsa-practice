# Binary Search Tree

A Binary Search Tree is used for organizing and storing data in a sorted manner. Each node in a Binary Search Tree has at most two children, a left child and a right child, with the left child containing values less than the parent node and the right child containing values greater than the parent node. This hierarchical structure allows for efficient searching, insertion, and deletion operations on the data stored in the tree.

- Elements have leaves, "nil"
- Height of tree is (height of left + height of right/ max (of either side)) +1

### Find

Checking if less than or greater than to know what side of the tree to search, and etc.

### Delete

Deleting a node, tree extends to child node beyond deletion. If deleting a root node, the node to the right reaches to the left until it hits a node with a NIL. For a successor, at least one child must be NIL.

### Tree Traversal

(iterators, map, set, dictionary)

- Inorder Travesal goes to left child as far down as it can go, then back to node, then right; sorted order

```python
def inorder_traversal(self):
    if self.left:
        self.left.inorder_traversal()
    print(self.value)
    if self.right:
        self.right.inorder_traversal()
```

- Preorder Travesal, first node, then left, then right

```python
def preorder_traversal(self):
    print(self.node)
    if self.left:
        self.left.preorder_traversal()
    if self.right:
        self.right.preorder_traversal()
```

- Postorder Traversal, first left, then right, then node

```python
def postorder_traversal(self):
    if self.left:
        self.left.postorder_traversal()
    if self.right:
        self.right.postorder_traversal()
    print(self.node)
```

Find

```python
def find(self, value):
    if value < self.value:
        if self.left is None:
            return False
        else:
            return self.left.find(value)
    elif value > self.value:
        if self.right is None:
            return False
        else:
            return self.right.find(value)
    else:
        return True
```
