# Greatest common divisor by Euclidian algorithm

def get_gcd(x: int, y: int) -> int:
    """
    Calculating Greatest Common Divisor
    using Euclidian algorithm
    """
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


# print(f"GCD = {get_gcd(15, 64)}")


def test_gcd_func(func: object, x: int, y: int, gcd_out: int) -> int:
    test_out = func(x, y) == gcd_out
    return test_out

print(f"Test 01 result: {test_gcd_func(get_gcd, 21, 35, 7)}")
print(f"Test 02 result: {test_gcd_func(get_gcd, 327, 801, 3)}")
print(f"Test 03 result: {test_gcd_func(get_gcd, 26, 260, 26)}")
print(f"Test 04 result: {test_gcd_func(get_gcd, 43, 433, 1)}")