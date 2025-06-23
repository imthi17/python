import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variable
x = sp.symbols('x')

# Define the function
f = x**3 - 2*x**2 + x + 1

# Calculate the derivative
f_prime = sp.diff(f, x)

# Convert the function and derivative to NumPy functions
f_np = sp.lambdify(x, f, 'numpy')
f_prime_np = sp.lambdify(x, f_prime, 'numpy')

# Generate x values
x_vals = np.linspace(-1, 3, 400)

# Calculate corresponding y values
y_vals = f_np(x_vals)
y_prime_vals = f_prime_np(x_vals)

# Create a figure and axis
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# Plot the function
ax[0].plot(x_vals, y_vals, label='f(x)')
ax[0].set_title('Function')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].legend()

# Plot the derivative
ax[1].plot(x_vals, y_prime_vals, label="f'(x)")
ax[1].set_title("Derivative")
ax[1].set_xlabel('x')
ax[1].set_ylabel("f'(x)")
ax[1].legend()

# Layout so plots do not overlap
fig.tight_layout()

plt.show()

print("Function: ", f)
print("Derivative: ", f_prime)


