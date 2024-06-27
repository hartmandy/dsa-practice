# Problem 3

We are given three subsets of numbers 𝐴,𝐵,𝐶⊆{0,…,𝑛}. Design an algorithm that runs in worst case time Θ(𝑛log(𝑛)) that checks if there exists numbers 𝑛1,𝑛2 in 𝐴,𝐵, respectively and number 𝑛3 in 𝐶 such that 𝑛1+𝑛2=𝑛3.

Hint: Convert the set 𝐴={𝑛0,𝑛1,…,𝑛𝑘} into the polynomial 𝑝𝐴(𝑥): 𝑥𝑛0+𝑥𝑛1+⋯+𝑥𝑛𝑘. Suppose 𝑝𝐴(𝑥),𝑝𝐵(𝑥) are polynomials obtained from the sets 𝐴,𝐵 respectively, interpret what the product 𝑝𝐴(𝑥)×𝑝𝐵(𝑥) signifies. Use this to complete an algorithm for the problem at hand that runs in 𝑛log(𝑛) time.

```python
# inputs sets a, b, c
# return True if there exist n1 in a, n2 in B such that n1+n2 in C
# return False otherwise
# number n which signifies the maximum number in a, b, c
# here is a useful reference to set data structure in python
# https://docs.python.org/3/tutorial/datastructures.html#sets
def check_sum_exists(a, b, c, n):
    a_coeffs = [0]*n
    b_coeffs = [0]*n
    # convert sets a, b into polynomials as provided in the hint
    # a_coeffs and b_coeffs should contain the result
    # your code here

    # multiply them together
    print ("a_coeffs . ", a_coeffs)
    print ("b_coeffs . ", b_coeffs)
    c_coeffs = polynomial_multiply(a_coeffs, b_coeffs)
    print("Co-efficients of the testcase are")
    coeffs_copy = []
    for num in c_coeffs:
        if(abs(num-0) < abs(num-1)):
            coeffs_copy.append(0)
        elif(abs(num-1) < abs(num-2)):
            coeffs_copy.append(1)
        else:
            coeffs_copy.append(2)
    print(coeffs_copy)
    # use the result to solve the problem at hand
    # your code here

    # return True/False
```
