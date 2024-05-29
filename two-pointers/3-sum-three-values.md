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

- Sort array
- enumerate returns pairs of index and value
- at each iteration we're checking triplet of index, low, and high
- if it equals target return True
- if greater than the target we decrement high
- if less than the target we increment low.
