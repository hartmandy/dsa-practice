## Remove nth Node from End of List

❔Given a singly linked list, remove the nth node from the end of the list and return its head.

```python
def remove_nth_last_node(head, n):
   dummy = fast = slow = LinkedListNode(0, next=head)

 # move fast pointer ahead n steps
   for _ in range(n):
    fast = fast.next

 # while fast pointer can move, move slow pointer as well
   while fast.next:
      fast = fast.next
      slow = slow.next

 # relink to next node
   slow.next = slow.next.next

   return dummy.next
```

- Create a dummy node to handle edge cases (like removing the first node)
- Initialize two pointers (fast and slow) at the dummy node
- Move fast pointer ahead n steps
- Move both pointers until first reaches the end.
- Remove the target node by adjusting the second pointer's next reference.
- Return the head of the modified list.

Video: https://www.youtube.com/watch?v=je2i2Yt4pwc
