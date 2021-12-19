# Greatest common divisor by Euclidian algorithm

def get_gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x

print(f"GCD = {get_gcd(35, 21)}")

def test_gcd_func(func):

