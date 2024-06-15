# Karatsuba's Multiplication Algorithm

Given two binary strings that represent value of two integers, find the product of two strings. For example, if the first bit string is “1100” and second bit string is “1010”, output should be 120.

For simplicity, let the length of two strings be same and be n.

A Naive Approach is to follow the process we study in school. One by one take all bits of second number and multiply it with all bits of first number. Finally add all multiplications. This algorithm takes O(n^2) time.

Using Divide and Conquer, we can multiply two integers in less time complexity. We divide the given numbers in two halves. Let the given numbers be X and Y.

For simplicity let us assume that n is even

```
X =  Xl*2n/2 + Xr    [Xl and Xr contain leftmost and rightmost n/2 bits of X]
Y =  Yl*2n/2 + Yr    [Yl and Yr contain leftmost and rightmost n/2 bits of Y]
```

The product XY can be written as follows.

```
XY = (Xl*2n/2 + Xr)(Yl*2n/2 + Yr)
   = 2n XlYl + 2n/2(XlYr + XrYl) + XrYr
```

etc... https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/

Video: https://www.youtube.com/watch?v=LCY4dnm88oI
