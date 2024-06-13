# Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

```python
    def moveZeroes(self, nums):
        # set left pointer, right moves throughout range
        left = 0

        for right in range(len(nums)):
            # if space to continue moving, swap zeroes to right side, increment left until end
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
```
