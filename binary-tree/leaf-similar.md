# Leaf-Similar Tree

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

```python
def leafSimilar(self, root1, root2):
# depth first search
    def dfs(root, leaf):
    if not root:
    return

# looking for children, once we reach leaf, add value to return list
        if not root.left and not root.right:
            leaf.append(root.val)
            return

        dfs(root.left, leaf)
        dfs (root.right, leaf)

    leaf1, leaf2 = [], []
    dfs(root1, leaf1)
    dfs(root2, leaf2)
    return leaf1 == leaf2
```
