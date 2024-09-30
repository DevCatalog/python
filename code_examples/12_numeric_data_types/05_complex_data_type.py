# Using the complex Function
complex_num1 = complex(3, 2)  # (3 + 2j)
complex_num2 = complex(1)  # Real part only (1 + 0j)
pure_imaginary = complex(0, 5)  # Imaginary part only (0 + 5j)

# Using Literal Notation
z = 5 + 4j  # Equivalent to complex(5, 4)
print("Real =", z.real)  # Output: 5.0
print("Imaginary =", z.imag)  # Output: 4.0

# Arithmetic operations
z1 = complex(2, 4)  # 2 + 4j
z2 = 1 - 2j
print(z1 + z2)  # Addition
print(z1 - z2)  # Subtraction
print(z1 * z2)  # Multiplication
print(z1 / z2)  # Division
