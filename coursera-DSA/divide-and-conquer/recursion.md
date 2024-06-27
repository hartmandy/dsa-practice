# Recursion, Recurrence

## Recursion

In divide-and-conquer algorithms, in the recursive case you

- Divide the problem into one or more subproblems that are smaller instances of the same problem.
- Conquer the subproblems by solving them recursively.
- Combine the subproblem solutions to form a solution to the original problem.

## Recurrence

A recurrence is an equation that describes a function in terms of its value on other, typically smaller, arguments.The general form of a recurrence is an equation or inequality that describes a function over the integers or reals using the function itself.

- In the substitution method, you guess the form of a bound and then use mathematical induction to prove your guess correct and solve for constants. This method is perhaps the most robust method for solving recurrences, but it also requires you to make a good guess and to produce an inductive proof.
- The recursion-tree method models the recurrence as a tree whose nodes represent the costs incurred at various levels of the recursion. To solve the recurrence, you determine the costs at each level and add them up, perhaps using techniques for bounding summations Even if you don’t use this method to formally prove a bound, it can be helpful in guessing the form of the bound for use in the substitution method.
- The master method is the easiest method, when it applies. It characterizes a divide-and-conquer algo rithm that creates a subproblems, each of which is 1=b times the size of the original problem, using f .n/ time for the divide and combine steps. To apply the master method, you need to memorize three cases, but once you do, you can easily determine asymptotic bounds on running times for many divide-and-conquer algorithms.
- The Akra-Bazzi method is a general method for solving divideand-conquer recurrences. Although it involves calculus, i t can be used to attack more complicated recurrences than those addressed by the master method.
