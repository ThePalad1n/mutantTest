from Polynomial import Polynomial
from mutation_operators import (mut_ops, modify_coefficients, invert_arithmetic_operations, remove_method)


def test_coefficient_modification():
    original_poly = Polynomial([3, 0, 2])
    modified_poly = mut_ops.modify_coefficients(original_poly)
    
    # The test checks if the coefficients of the original and modified polynomials are different
    assert original_poly.coefficients != modified_poly.coefficients, "Coefficient modification mutation not detected"


def test_arithmetic_operation_inversion():
    mut_ops.invert_arithmetic_operations(Polynomial)  # Apply mutation

    poly1 = Polynomial([1, 2])
    poly2 = Polynomial([3, 4])
    sum_poly = poly1 + poly2  # Should perform subtraction due to mutation

    expected_result = Polynomial([-2, -2])  # Expected result if subtraction is performed
    assert sum_poly.coefficients == expected_result.coefficients, "Arithmetic operation inversion mutation not detected"

def test_remove_method():
    remove_method(Polynomial, 'evaluate')
    poly = Polynomial([1, 2])

    # Assert that the evaluate method is removed
    assert not hasattr(poly, 'evaluate')