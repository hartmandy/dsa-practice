# Two Pointers

**Tracking two places in an array at the same time**

- Linear data structure: The input data can be traversed in a linear fashion, such as an array, linked list, or string.
- Process pairs: Process data elements at two different positions simultaneously.
- Dynamic pointer movement: Both pointers move independently of each other according to certain conditions or criteria. In addition, both pointers might move along the same or two different data structures.

Real world problem: Memory management: The two pointers pattern is vital in memory allocation and deallocation.

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

## Sum of Three Values

❔Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

```python
def find_sum_of_three(nums, target):
   nums.sort()
   for index, value in enumerate(nums):
      low = index +1
      high = len(nums)-1
      while low<high:
         current_sum = value + nums[low] + nums[high]
         if current_sum == target:
            return True
         elif current_sum > target:
            high-=1
         else:
            low+=1

   return False
```

Sort array, enumerate returns pairs of index and value, at each iteration we're checking triplet of index, low, and high and if it equals target return True, if greater than the target we decrement high, if less than the target we increment low.

## Remove nth Node from End of List

### Linked List

Linked list is a data structure similar to array in a sense that it stores bunch of items. But unlike array, linked lists are not stored in contiguous memory locations. They are instead chained by an element storing address location of next element. This makes insertion very easy. Also unlike dynamic arrays you don't have to pre-allocate some memory capacity.

Video: https://www.youtube.com/watch?v=qp8u-frRAnU

```python
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
```

❔Given a singly linked list, remove the nth node from the end of the list and return its head.

```python

```
