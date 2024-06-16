# Problem 1: Max Subarray Problem

Recall the max subarray problem presented in class. We used divide and conquer method to derive a Θ(𝑛log(𝑛))
worst case time algorithm to solve it.

In this assignment, we would like you to solve this problem in Θ(𝑛)
time. I.e, your algorithm should be able to compute the result by just iterating through the array and keeping track of some quantities.

Let [a0, a1,....,ak] be a python array (list) of size k + 1. Here is the idea:

As we iterate index i from 0 to k (inclusive), track a quantity minSoFar that is the minimum of the array so far from 0 to i-1. Initialize minSoFar to +infinity (In python you can say float('inf') to get a number that represents ∞).
Consider the difference a[i] - minSoFar. Calculate the maximum such difference when iterating over the entire array.
Convince yourself that this will yield the overall solution to the max subarray problem with a complexity of Θ(𝑛).
