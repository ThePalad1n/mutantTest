# Example usage script

from Polynomial import Polynomial
import mutation_operators as mut_ops

# Original Polynomial
poly1 = Polynomial([3, 0, 2])
print("Original Polynomial:", poly1)

# Apply Coefficient Modification
modified_poly = mut_ops.modify_coefficients(poly1)
print("Modified Coefficients:", modified_poly)

# Invert Arithmetic Operations in Polynomial Class
mut_ops.invert_arithmetic_operations(Polynomial)
poly2 = Polynomial([1, -1])
sum_poly = poly1 + poly2  # This will now perform subtraction
print("Inverted Operation Sum:", sum_poly)
