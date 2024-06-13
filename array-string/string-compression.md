# String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

```python
    def compress(self, chars):
        read, write = 0, 0

# we want to look at two characters and see if they're equal, if so we increment count
        while read < len(chars):
            start = read
            while read < len(chars) and chars[read] == chars[start]:
                read += 1
            chars[write] = chars[start]
            write += 1
# if they're not equal, add character and count as a string and move to next character

# if compressed string isn't less than original string, just return original
            if read - start > 1:
                for digit in str(read-start):
                    chars[write] = digit
                    write += 1
        return write
```
