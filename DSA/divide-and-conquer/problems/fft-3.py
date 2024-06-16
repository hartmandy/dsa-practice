from numpy.fft import fft, ifft
import numpy as np

def polynomial_multiply(a_coeff_list, b_coeff_list):
    A = fft(a_coeff_list)
    B = fft(b_coeff_list)
    
    C = A * B
    
    c_coeff_list = ifft(C)
    c_coeff_list_real = np.round(c_coeff_list.real).astype(int)
    
    return c_coeff_list_real

def check_sum_exists(a, b, c, n):
    a_coeffs = [0]*n
    b_coeffs = [0]*n 
    # convert sets a, b into polynomials as provided in the hint
    # a_coeffs and b_coeffs should contain the result
    a_coeffs = [1 if i in a else 0 for i in range(n)]
    b_coeffs = [1 if i in b else 0 for i in range(n)]

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

    exp = [i for i in range(len(c_coeffs)) if c_coeffs[i] > 0]

    # use the result to solve the problem at hand
    for num in c:
        if not any(i + j == num for i in a for j in b):
            return False
    
    return True


    # I'm stumped! I got test 1 and 4 to pass on my local computer, but hitting a wall for test 2 and 3

# Testing the function
print('-- Test 1 --')
a = set([1, 2, 10, 11])
b = set([2, 5, 8, 10])
c = set([1, 2, 5, 8])
assert not check_sum_exists(a, b, c, 12), f'Failed Test 1: your code returned true when the expected answer is false'
print('Passed')

print('-- Test 2 --')
a = set([1, 2, 10, 11])
b = set([2, 5, 8, 10])
c = set([1, 2, 5, 8, 11])
assert check_sum_exists(a, b, c, 12), f'Failed Test 2: your code returns false but note that 1 in a + 10 in b = 11 in c '
print('Passed')

print('-- Test 3 --')
a={1, 4, 5, 7, 11, 13, 14, 15, 17, 19, 22, 23, 24, 28, 34, 35, 37, 39, 42, 44}
b={0, 1, 4, 9, 10, 11, 12, 15, 18, 20, 25, 31, 34, 36, 38, 40, 43, 44, 47, 49}
c={3, 4, 5, 7, 8, 10, 19, 20, 21, 24, 31, 35, 36, 37, 38, 39, 42, 44, 46, 49}
assert check_sum_exists(a, b, c, 50), f'Failed Test 3: your code returns False whereas the correct answer is true eg., 4 + 0 = 4'

print('-- Test 4 --')
a={98, 2, 99, 40, 77, 79, 87, 88, 89, 27}
b={64, 66, 35, 69, 70, 40, 76, 45, 12, 60}
c={36, 70, 10, 44, 15, 16, 83, 20, 84, 55}
assert not check_sum_exists(a, b, c, 100), f'Failed Test 4: your code returns True whereas the correct answer is False'

print('All Tests Passed (15 points)!')
