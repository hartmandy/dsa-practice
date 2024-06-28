# Remove Stars From a String

You are given a string s, which contains stars \*.

In one operation, you can:

- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.
- Return the string after all stars have been removed.

Note: The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

```python
    def removeStars(self, s):
        stack = []

# for every char in string, check for wild card
        for c in s:
            if c == "*":
                stack and stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
```
