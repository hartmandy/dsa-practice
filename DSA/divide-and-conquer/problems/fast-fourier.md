# Problem 2

We studied polynomial multiplication using FFT in class. Recall the algorithm given two polynomials 𝑎(𝑥)=𝑎0+𝑎1𝑥+⋯+𝑎𝑛−1𝑥𝑛−1 and 𝑏(𝑥)=𝑏0+𝑏1𝑥+⋯+𝑏𝑚−1𝑥𝑚−1.

Pad the coefficients of 𝑎,𝑏 with zero coefficients to make up two polynomials of degree 𝑚+𝑛−2 (expected size of the result).
Compute FFTs of [𝑎0,…,𝑎𝑛−1,0,…,0] and [𝑏0,…,𝑏𝑛−1,0,…,0].
Let [𝐴0,…,𝐴𝑚+𝑛−2] and [𝐵0,…,𝐵𝑚+𝑛−2] be the resulting FFT sequences.
Multiply the FFT sequences: [𝐴0×𝐵0,…,𝐴𝑚+𝑛−2×𝐵𝑚+𝑛−2].
Compute the inverse FFT to obtain the polynomial 𝑐(𝑥)=𝑎(𝑥)𝑏(𝑥).
First implement polynomial multiplication using FFT. For convenience, please use the numpy package in python which implements functions numpy.fft.fft and numpy.fft.ifft. The advantages include efficient computation of FFT for sizes of inputs that are not powers of two.

### Brief Illustration of Numpy `fft` and `ifft` functions.

```python
from numpy.fft import fft, ifft
from numpy import real, imag

#fft --> computes fft of a list or numpy array
#ifft -> computes inverse fft of list or numpy array

# Create a list
lst0 = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
# Compute its fft
fft_lst0 = fft(lst0)
print(f'FFT of {lst0} is\n \t {fft_lst0}' )
# Compute iverse fft
ifft_lst0 = ifft(fft_lst0)
print(f'After ifft: {ifft_lst0}' )
# Check that all the imaginary parts are tiny in the ifft result
# Note that they will not be zero due to floating point error
assert(all([abs(imag(x))<= 1E-10 for x in ifft_lst0])), 'Something went wrong -- we should not have complex parts to the ifft result'
# Extract the real parts
print('Note that we can suppress the vanishingly small complex cofficients')
fix_ifft_lst0 = [real(x) for x in ifft_lst0]
print(f'After converting back to float: {fix_ifft_lst0}')
```

Implement the polynomial_multiply function below.

```python
from numpy.fft import fft, ifft
from numpy import real, imag

def polynomial_multiply(a_coeff_list, b_coeff_list):
    # Return the coefficient list of the multiplication
    # of the two polynomials
    # Returned list must be a list of floating point numbers.
    # Please convert list from complex to reals by using the
    # real function in numpy.
    # your code here
```
