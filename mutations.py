from Polynomial import Polynomial
import mutation_operators as mut_ops

# Original Polynomial
original_poly = Polynomial([3, 0, 2])
print("Original Polynomial:", original_poly)


# Mutant with Modified Coefficients
mutant_coeff_mod = mut_ops.modify_coefficients(original_poly)
print("Mutant with Modified Coefficients:", mutant_coeff_mod)


# Invert Arithmetic Operations in Polynomial Class
mut_ops.invert_arithmetic_operations(Polynomial)

# Creating a new instance to demonstrate the effect of the mutation
poly1 = Polynomial([1, 2])
poly2 = Polynomial([3, 4])
sum_poly = poly1 + poly2  # This will now perform subtraction instead of addition
print("Mutant with Inverted Operations (Sum):", sum_poly)
