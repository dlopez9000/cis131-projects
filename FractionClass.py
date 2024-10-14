# Darlene Lopez
# CIS 131
# This program uses The Python Standard Library module which provides a Fraction class and is view only.

from fractions import Fraction

fraction1 = Fraction(5, 6)  # Demonstrating Fraction operations
fraction2 = Fraction(9, 8)  # Can change to any number here

# Adding two fractions
fraction_add = fraction1 + fraction2
print(f"Adding {fraction1} and {fraction2} gives {fraction_add}")

# Subtracting two fractions
fraction_subtract = fraction1 - fraction2
print(f"Subtracting {fraction2} from {fraction1} gives {fraction_subtract}")

# Multiplying two fractions
fraction_multiply = fraction1 * fraction2
print(f"Multiplying {fraction1} and {fraction2} gives {fraction_multiply}")

# Dividing two fractions
fraction_divide = fraction1 / fraction2
print(f"Dividing {fraction1} by {fraction2} gives {fraction_divide}")

# Converting fraction to float
fraction_to_float = float(fraction1)
print(f"The float value of {fraction1} is {fraction_to_float}")

# Demonstrating complex number operations and change to any number here
complex1 = complex(4, 6)
complex2 = complex(3, 5)

# Adding two complex numbers
complex_add = complex1 + complex2
print(f"Adding {complex1} and {complex2} gives {complex_add}")

# Subtracting two complex numbers
complex_subtract = complex1 - complex2
print(f"Subtracting {complex2} from {complex1} gives {complex_subtract}")

# Getting real and imaginary parts of the first complex number
complex1_real = complex1.real
complex1_imag = complex1.imag
print(f"The real part of {complex1} is {complex1_real} and the imaginary part is {complex1_imag}")
