import argparse
from typing import Optional


def find_roots(a: int, b: int, c: int) -> Optional[float | tuple[float, float]]:
    """
    Calculate the roots of the quadratic equation ax^2 + bx + c = 0.
    

    Parameters:
    a (int): Coefficient of x^2
    b (int): Coefficient of x
    c (int): Constant term

    Returns:
    Optional[float | tuple[float, float]]: A tuple containing two roots if they exist, a single root if there is one, or None if there are no real roots.
    """
    
    D = b**2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        return -b / (2 * a)
    else:
        return (-b + D**0.5) / (2 * a), (-b - D**0.5) / (2 * a)


def main() -> None:
    """
    Parse command-line arguments and find the roots of the quadratic equation.
    """
    parser = argparse.ArgumentParser(
        description="Find the roots of a quadratic equation ax^2 + bx + c = 0"
    )
    parser.add_argument("a", type=int, help="Coefficient a")
    parser.add_argument("b", type=int, help="Coefficient b")
    parser.add_argument("c", type=int, help="Coefficient c")

    args = parser.parse_args()

    roots = find_roots(args.a, args.b, args.c)
    print(f"The roots are: {roots}")


if __name__ == "__main__":
    main()

# here I took the code generated from the original def satement:
# def find_roots(a: int, b: int, c: int):
# and I asked it to:
# - add the abililty to run this with command line arguemnts
# - add docstrings
# - add type hints
# - change from Union to pipes for the typehints
# - format with Black
# It did all of this without issue and it's even helping with these comments.
