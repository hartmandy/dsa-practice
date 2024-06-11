# Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Examples:

- Input: candies = [2,3,5,1,3], extraCandies = 3
- Output: [true,true,true,false,true]
- Explanation: The current max value is 5 which is held by Kid 3

Kid 1, they will have 2 + 3 = 5 candies, which is greater or equal to the current max of 5.

Kid 2, they will have 3 + 3 = 6 candies, which is greater or equal to the current max of 5.

Kid 3, they will have 5 + 3 = 8 candies, which is greater or equal to the current max of 5.

Kid 4, they will have 1 + 3 = 4 candies, which is less than the current max of 5.

Kid 5, they will have 3 + 3 = 6 candies, which is greater or equal to the current max of 5.

```python
    def kidsWithCandies(self, candies, extraCandies):
# determine the max number in the array
        max_candies = max(candies)

 # compare each number + 3(extra) to the max number
        return [(current_number + extraCandies >= max_candies) for current_number in candies]
```
