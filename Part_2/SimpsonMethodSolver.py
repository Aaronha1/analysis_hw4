import numpy as np


def trapezoidal_method(func, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))  # First and last points
    for i in range(1, n):
        integral += func(a + i * h)  # Sum of middle points
    integral *= h
    return integral

# Given integral limits
a = 0
b = np.pi
# Number of segments
n = 4
# Function
func = lambda x: np.sin(x)

# Calculate integral using trapezoidal method
integral_approx = trapezoidal_method(func, a, b, n)
print("Approximated Integral using Trapezoidal Method:", integral_approx)

# Exact integral value
exact_integral = 2.0  # Integral of sin(x) from 0 to pi is 2
print("Exact Integral Value:", exact_integral)

# Calculate error
error = abs(exact_integral - integral_approx)
print("Error:", error)
