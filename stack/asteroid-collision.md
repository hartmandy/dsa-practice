# Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

```python
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
    # if stack isn't empty and asteroid on top of stack
    # is positive/ moving to the right
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
    # and account for if both are destroyed
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)

        return stack
```
