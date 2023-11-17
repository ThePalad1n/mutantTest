# mutation_operators.py

import random
from Polynomial import Polynomial

def modify_coefficients(poly, change_type='random'):
    """
    Modify the coefficients of a polynomial.
    
    :param poly: Polynomial object
    :param change_type: Type of modification ('random', 'add', 'remove')
    :return: Modified Polynomial object
    """
    new_coefficients = poly.coefficients.copy()

    if change_type == 'random':
        # Randomly change one coefficient
        index = random.randint(0, len(new_coefficients) - 1)
        new_coefficients[index] = random.randint(-10, 10)
    elif change_type == 'add':
        # Add a new coefficient
        new_coefficients.append(random.randint(-10, 10))
    elif change_type == 'remove':
        # Remove a coefficient if possible
        if len(new_coefficients) > 1:
            new_coefficients.pop()

    return Polynomial(new_coefficients)


def invert_arithmetic_operations(poly_class):
    """
    Invert arithmetic operations in Polynomial class.
    
    :param poly_class: Polynomial class
    :return: Modified Polynomial class with inverted operations
    """
    original_add = poly_class.__add__
    original_sub = poly_class.__sub__

    def new_add(self, other):
        return original_sub(self, other)

    def new_sub(self, other):
        return original_add(self, other)

    poly_class.__add__ = new_add
    poly_class.__sub__ = new_sub

    return poly_class

def remove_method(poly_class, method_name):
    """
    Remove a method from the Polynomial class.
    """
    if hasattr(poly_class, method_name):
        delattr(poly_class, method_name)

def change_return_type(poly_class, method_name, new_return):
    """
    Change the return type of a method in the Polynomial class.
    """
    original_method = getattr(poly_class, method_name)

    def modified_method(*args, **kwargs):
        original_method(*args, **kwargs)
        return new_return

    setattr(poly_class, method_name, modified_method)
