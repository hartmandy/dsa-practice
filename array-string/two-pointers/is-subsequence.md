# Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

```python
    def isSubsequence(self, s, t):
        i, j = 0, 0
# looking through each string and comparing chars, increment both
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
# j increments whether they're the same or not, so it's in if and else
            j += 1
# if we reach the end of the first string, and found a match in the second string
        return True if i == len(s) else False
```
