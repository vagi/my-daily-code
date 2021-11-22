# Source: https://stepik.org/lesson/415554/step/3?unit=405083


# Best option using slices
s = list(map(int, input().split()))
s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
print(*s)


# Better option
digits = [int(c) for c in input().split()]

for i in range(1, len(digits), 2):
    digits[i - 1], digits[i] = digits[i], digits[i - 1]

print(*digits)


# My code
# numbers = [int(num) for num in input().split()]
# if len(numbers) % 2 == 0:
#     for idx in range(0, len(numbers), 2):
#         numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
# else:
#     for idx in range(0, len(numbers[:-1]), 2):
#         numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
#
# print(*numbers)    # Unpacking the list object - *


# Input: 1 2 3 4 5
