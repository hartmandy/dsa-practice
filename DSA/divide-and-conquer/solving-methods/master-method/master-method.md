# Master Method

A master recurrence describes the running time of a divide-and-conquer algorithm that divides a problem of size n into a subproblems, each of size n=b < n. The algorithm solves the a subproblems recursively, each in T(n/b) time. The driving function f(n) encompasses the cost of dividing the problem before the recursion, as well as the cost of combining the results of the recursive solutions to subproblems. For example, the recurrence arising from Strassen’s algorithm is a master recurrence with a a= 7, b= 2 , and driving function f(n) = Theta n^2.
