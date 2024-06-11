# Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

- Example 1:
  Input: s = "hello"
  Output: "holle"
- Example 2:
  Input: s = "leetcode"
  Output: "leotcede"

```python
    def reverseVowels(self, s):
        # turn the string into a list, declare vowels, set two pointers
        lst = list(s)
        vowels = set('aeiouAEIOU')
        start, end = 0, len(s)-1

        # if start is not a vowel, increment start
        # if end is not a vowel, decrement end
        while (start < end):
            if (lst[start] not in vowels):
                start += 1
            elif (lst[end] not in vowels):
                end -=1
        # if they are vowels, swap and increment to next
            else:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1

        return "".join(lst)
```
