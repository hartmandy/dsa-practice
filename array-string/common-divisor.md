# Greatest common divisor of strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # Get the lengths of both strings
        len1, len2 = len(str1), len(str2)

        # Helper function to check if a given length can divide both strings perfectly
        def is_divisor(length):
            # If length is not a divisor of either string length, return False
            if len1 % length != 0 or len2 % length != 0:
                return False
            # Calculate how many times the substring of given length repeats to form the original strings
            factor1, factor2 = len1 // length, len2 // length
            # Check if repeating the substring forms the original strings
            return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2

        # Try every length from the smaller string down to 1
        for length in range(min(len1, len2), 0, -1):
            # If this length can divide both strings, return the substring of this length
            if is_divisor(length):
                return str1[:length]

        # If no common divisor is found, return an empty string
        return ""

```
