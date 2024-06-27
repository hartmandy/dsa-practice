def maxSubArray(a):
    n = len(a)
    if n == 1:
        return 0
    
    # minSoFar starts at ∞ to ensure any element in the array will be less than it 
    # Same with maxDifference to ensure any calculated difference will be greater
    
    minSoFar = float('inf')
    maxDifference = -float('inf')
    
    # At each loop, minSoFar is updated to be the smallest value encountered so far.
    # The difference a[i] - minSoFar, to find the potential maxsubarray sum ending at the current element
    # maxDifference is updated if this difference is greater than the previously recorded maximum
    
    for i in range(n):
        minSoFar = min(minSoFar, a[i])
        maxDifference = max(maxDifference, a[i] - minSoFar)
    
    return maxDifference

# Test cases
assert(maxSubArray([100, -2, 5, 10, 11, -4, 15, 9, 18, -2, 21, -11]) == 25), 'Test 1 failed'
assert(maxSubArray([-5, 1, 10, 4, 11, 4, 15, 9, 18, 0, 21, -11]) == 26), 'Test 2 failed'
assert(maxSubArray([26, 0, 5, 18, 11, -1, 15, 9, 13, 5, 16, -11]) == 18), 'Test 3 failed'

from random import randint

def get_random_array(n):
    assert(n > 100)
    lst = [randint(0, 25) for j in range(n)]
    lst[0] = 1000
    lst[10] = -15
    lst[25] = 40
    lst[n-10] = 60
    lst[n-3]= -40
    return lst

assert(maxSubArray(get_random_array(50000)) == 75), 'Test on large random array 50000 failed'
assert(maxSubArray(get_random_array(500000)) == 75), 'Test on large random array of size 500000 failed'
print('All tests passed (10 points!)')