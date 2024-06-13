# Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5] Output: true
Explanation: Any triplet where i < j < k is valid.

```python
    def increasingTriplet(self, nums):
        num_i = num_j = float('inf')

# checking if i < j < k, if that's the case return True, if it isn't true, the next number in the array is now i and we check again for i < j < k

        for num in nums:
            if num <= num_i:
                num_i = num
            elif num <= num_j:
                num_j = num
            else:
                return True
        return False
```
