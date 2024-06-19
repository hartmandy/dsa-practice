# Container with Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

```python
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height)-1

        while l < r:
# find max area
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
# if right is greater, we decrement right until they meet
    # elif height[l] > height[r]:
    #     r -= 1
            else:
                r -= 1
        return res
```
