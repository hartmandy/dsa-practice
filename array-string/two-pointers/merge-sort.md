# Mergesort

The main idea behind merge sort of a list of size `n` is to

1. Split the list into two "sublists" of size `n/2`
2. Sort the sublists
3. Merge the result.

We maintain two indices `i1` and `i2`,
where `i1` is an index for `lst1` and `i2` is an index for `lst2`.

- If `lst1[i1] <= lst2[i2]` then we take the element `lst1[i1]` and append it at the end of our output list. We then advance the index `i1`.
- Alternatively, `lst1[i1] > lst2[i2]`, then we take `lst2[i2]` and append it to the end of our output list. We then advance the index `i2`.

If in the process above, we run over the end of the list, we simply copy the remaining elements of the other list.

```python
def mergeLists(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    if n1 == 0: # lst1 is empty
        return list(lst2)
    elif n2 == 0:
        return list(lst1)
    else:
        output_lst = []
# This is the list we will return
        i1 = 0
        i2 = 0
        while (i1 < n1 or i2 < n2):
            if i1 < n1 and i2 < n2:
# We are processing both lists
                if (lst1[i1] <= lst2[i2]):
# lst[i1] is the smaller elt
                    output_lst.append(lst1[i1])
# append to end of output list
                    i1 = i1 + 1
# advance index i1
                else:
                    output_lst.append(lst2[i2])
# append to end of output list
                    i2 = i2 + 1
# advance index i2
            elif i1 < n1:
# We have run past the end of lst2
                output_lst.append(lst1[i1])
# append lst1 to end of output list
                i1 = i1 + 1
            else:
# We have run past the end of lst1
                output_lst.append(lst2[i2])
# append lst2 to end of output list
                i2 = i2 + 1
        return output_lst
```
