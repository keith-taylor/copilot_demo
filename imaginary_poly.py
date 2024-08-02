"""
This function will return the roots, real or imaginary, of a quadratiic function.
"""

import cmath
from typing import Optional


def find_roots(a: int, b: int, c: int) -> Optional[float | tuple[float, float]]:
    """
    Calculate the roots of the quadratic equation ax^2 + bx + c = 0.


    Parameters:
    a (int): Coefficient of x^2
    b (int): Coefficient of x
    c (int): Constant term

    Returns:
    Optional[float | tuple[float, float]]: A tuple of complex numbers.
    """

    D = b**2 - 4 * a * c
    if D < 0:
        return (-b + cmath.sqrt(D)) / (2 * a), (-b - cmath.sqrt(D)) / (2 * a)
    elif D == 0:
        return -b / (2 * a)
    else:
        return (-b + cmath.sqrt(D)) / (2 * a), (-b - cmath.sqrt(D)) / (2 * a)


print(find_roots(1, 2, 3))

# i had to do the import Optional stuff, but other than that very good
