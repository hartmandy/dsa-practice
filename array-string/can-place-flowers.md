# Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Examples:

- Input: flowerbed = [1,0,0,0,1], n = 1
  Output: true
- Input: flowerbed = [1,0,0,0,1], n = 2
  Output: false

Note:

- No-adjacent means that there are no 1's next to each other.
  Something like [1,0,1,0,1] or [1,0,0,1] are valid while [1,0,1,1] or [1,1] are not.

- Additionally, n can be less than or equal the maximum amount of flowers you can place.
  Something like [0,0,0,0,0] can have at most 3 flowers: [1,0,1,0,1], so any n such that n<=3 should return true.

```python
    def canPlaceFlowers(self, flowerbed, n):
        # append 0 to start and end
        flower = [0] + flowerbed + [0]

        # ignore first and last in array, added zeroes
        for i in range(1, len(flower)- 1):
            if flower[i-1] == 0 and flower[i] == 0 and flower[i+1] == 0:
                flower[i] = 1
                n-=1
        return n<= 0
```
