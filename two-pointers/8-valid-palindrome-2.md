## Valid Palindrome II

❔ Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.

```python
def is_palindrome(s):
    def is_valid_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_valid_palindrome(s, left + 1, right) or is_valid_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True
```

Video: https://www.youtube.com/watch?v=JrxRYBwG6EI
