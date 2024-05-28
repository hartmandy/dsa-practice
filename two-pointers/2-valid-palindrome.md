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

Defined the two pointers, wrote a while loop and converged the two pointers, each iteration checking if start and end points are not equal and returning False if they arent. If we get through the while loop without returning False, we return True.
