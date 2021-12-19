# Greatest common divisor by Euclidian algorithm
from typing import Callable


def get_gcd(x: int, y: int) -> int:
    """
    Calculating Greatest Common Divisor
    using Euclidian algorithm
    """
    if x < y:
        x, y = y, x

    try:
        x % y
        while y:
            x, y = y, x % y
        return x
    except ZeroDivisionError:
        print("It's not possible to divide by 0")


# print(f"GCD = {get_gcd(0, 75)}")


def test_gcd_func(func: Callable[[int, int], int], x: int, y: int, gcd_out: [int, None]) -> int:
    test_out = func(x, y) == gcd_out
    return test_out


print(f"Test 01 result: {test_gcd_func(get_gcd, 21, 35, 7)}")
print(f"Test 02 result: {test_gcd_func(get_gcd, 0, 73, None)}")
print(f"Test 03 result: {test_gcd_func(get_gcd, 26, 260, 26)}")
print(f"Test 04 result: {test_gcd_func(get_gcd, 43, 433, 1)}")