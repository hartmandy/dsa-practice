# Max Subarray

Like solving for the best time to buy and sell stock, looking in an array for the lowest and highest price, but no short sell (have to buy before you can sell, visible in time on a graph)

With a max subarray, we can split the array in half and we can find the lowest on the left array and the highest on the right away. DIVIDE - RECURSE - COMBINE

### Leetcode 53

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1: Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

(Linear approach O(n), divide and conquer approach "Kadane's algorithm" O(logn))

```python
psuedocode:
def kadane(A):
    max_current = max_global = A[0]
    for i from 1 to (len(A) - 1):
        max_current = max(A[i], max_current + A[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
```

For each element A[i], update max_current to be the maximum of A[i] and max_current + A[i]. This step decides whether to add the current element to the existing subarray (max_current + A[i]) or start a new subarray with the current element (A[i]).

```python
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0

        for n in nums:
        # to disregard negative number, set to zero
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
```

For each element n in nums:
If curSum is less than 0, reset curSum to 0. This step ensures that any negative sum accumulated so far is disregarded, as it would reduce the sum of any new subarray starting from the next element.
Add the current element n to curSum.
Update maxSub to be the maximum of maxSub and curSum. This keeps track of the maximum sum encountered so far.

---

#### Quiz answers for Max Subarray

- The output .to the max subarray .problem should be 18 - (-4) = 22
- The minimum element of the first half of the array is -4 and maximum element of the second half of the array is 18. These in turn form the result for the max subarray problem which is 22.
- The divide and conquer algorithm will compute the result of max subarray problem on the first half of the array, which in this instance yields the value 18

---

- The case when 𝑛 ≤ 2 n≤2 represents the constant amount of work needed to find the max subarray for input arrays of size 1 or 2.
- The Θ(𝑛) Θ(n) term in the recurrence for 𝑛>2 n>2 represents the work to find minimum of first half and maximum of second half.
- The recurrence assumes that 𝑛n is a power of two, since repeated division by 2 2 can yield fractional results otherwise.
- The recurrence and the running time are identical to that obtained for the mergesort algorithm covered earlier in course 1 of this specialization.
