import numpy as np
import sympy as sp

def trapezoidal_method(func, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))  # First and last points
    for i in range(1, n):
        integral += func(a + i * h)  # Sum of middle points
    integral *= h
    return integral

# Function
x = sp.symbols('x')
func = sp.sin(x)

# Given integral limits
a = 0
b = np.pi

# Number of segments
n = 4

# Exact integral value
exact_integral = sp.integrate(func, (x, a, b))

# Calculate integral using trapezoidal method
integral_approx = trapezoidal_method(sp.lambdify(x, func), a, b, n)
print("Approximated Integral using Trapezoidal Method:", integral_approx)

print("Exact Integral Value:", exact_integral)

# Calculate error
error = abs(exact_integral - integral_approx)
print("Error:", error)
