# Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
# set both pointers to the start of each string and start output
        i, j = 0, 0
        result = []

# while we have characters in both strings,append index of each into output and increment through
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
# if characters are still left, append remaining characters
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)
```
