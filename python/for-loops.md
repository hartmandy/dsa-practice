## For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)
```

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

```python
for x in range(6):
  print(x)
```

You can specify start and end numbers by passing in, like (2, 10) to override default. You can add a third number as the increment, like (2, 10, 2) would display 2-10 in increments of 2.

```python
for x in range(2, 10, 2)
    print(x)
```

## Else in For Loop

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

## Nested Loops

A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop":

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
```
