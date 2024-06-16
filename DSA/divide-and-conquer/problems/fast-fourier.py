from numpy.fft import fft, ifft
from numpy import real, imag

def polynomial_multiply(a_coeff_list, b_coeff_list):
    n = len(a_coeff_list)
    m = len(b_coeff_list)
    size = m + n - 1
    
    # Pad the coefficients of $a, b$ with zero coefficients to make up two polynomials of degree $m + n - 2$ 
    a_coeff_list_padded = a_coeff_list + [0] * (size - n)
    b_coeff_list_padded = b_coeff_list + [0] * (size - m)
    
    # Compute FFTs of $[a_0, \ldots, a_{n-1}, 0 , \ldots, 0 ]$ and $[b_0, \ldots, b_{n-1}, 0, \ldots, 0 ]$. 
    A = fft(a_coeff_list_padded)
    B = fft(b_coeff_list_padded)
    
    # Multiply the FFT sequences: $[ A_0 \times B_0, \ldots, A_{m+n-2} \times B_{m+n-2}]$.
    C = [A[i] * B[i] for i in range(size)]
    
    # Compute the inverse FFT to obtain the polynomial $c(x) = a(x) b(x)$.
    c_coeff_list = ifft(C)
    
    # Convert result to real numbers
    c_coeff_list_real = [real(x) for x in c_coeff_list]
    
    return c_coeff_list_real