## Valid Palindrome

❔ Write a function that takes a string, s, as an input and determines whether or not it is a palindrome (a word, phrase, or sequence of characters that reads the same backward as forward)

```python
def is_palindrome(s):
  start = 0
  end = len(s)-1
  while start<end:
    if s[start] is not s[end]:
      return False
    start+=1
    end-=1

  return True
```

- Initialize two pointers: start at the beginning and end at the end of the string.
- Use a while loop to move the pointers towards the center.
- Inside the loop, compare characters at start and end.
- If characters are not equal, return False.
- Move the pointers inward (increment start, decrement end).
- If the loop completes without finding a mismatch, return True.
