# Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```python
    def maxDepth(self, root):
# adding each node to a queue with index while traversing
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
# as we traverse we add to depth if there are children
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
```
