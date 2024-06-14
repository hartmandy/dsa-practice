# Binary Search

Binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.

```python
def binarySearchHelper(lst, elt, left, right):
    n = len(lst)
    if (left > right):
        return None # Search region is empty -- let us bail since we cannot find the element elt in the list.
    else:
        # If elt exists in the list, it must be between left and right indices.
        mid = (left + right)//2 # Note that // is integer division
        if lst[mid] == elt:
            return mid # BINGO -- we found it. Return its index signalling that we found it.
        elif lst[mid] < elt:
            # We search in the right part of the list
            return binarySearchHelper(lst, elt, mid+1, right)
        else: # lst[mid] > elt
            # We search in the left part of the list.
            return binarySearchHelper(lst, elt, left, mid-1)
```

Complexity Analysis

Thus, the initial search region size is 𝑛 , the size of the list. At each subsequent call, the search region shrinks by half of the previous search region.

Therefore, if we made 𝑘 iterations of binarySearchHelper, the search region would be at most 𝑛2𝑘 .

When the search region size is less than 1 , we have to stop since we would reach the condition left < right.

In the worst case therefore, binary search can run for k steps as long as 𝑛2𝑘≥1 .

On other words, 2𝑘≤𝑛 , i.e, 𝑘≤log2(𝑛) .

Each recursive call involves constant number of operations. Thus, we concluded that the running time is bounded from above by 𝑂(log(𝑛)) .

A similar analysis shows that for every 𝑛 , we can produce a list of size 𝑛 and a missing element such that the algorithm must take time proportional to log2(𝑛) to run. This lets us conclude that the running time must be Ω(log(𝑛)) in the worst case.

Combining, we get that the running time is Θ(log(𝑛)) .
