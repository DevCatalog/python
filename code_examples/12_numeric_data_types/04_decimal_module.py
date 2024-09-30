from decimal import Decimal

# Floats in Python can’t precisely represent all numbers.
a = 0.1
b = 0.2
c = a + b
print(c)  # 'c' should be 0.3

# The decimal module in Python can accurately represent decimal numbers.
a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c)  # 'c' should be 0.3
