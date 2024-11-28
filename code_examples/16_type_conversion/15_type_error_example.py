# Type Errors: Mismatched Data Types
x = "10"
y = 5
# result = x + y  # TypeError
result = int(x) + y  # Correct type conversion
print(result)
