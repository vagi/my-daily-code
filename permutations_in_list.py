# Source: https://stepik.org/lesson/415554/step/3?unit=405083

numbers = [int(num) for num in input().split()]
if len(numbers) % 2 == 0:
    for idx in range(0, len(numbers), 2):
        numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
else:
    for idx in range(0, len(numbers[:-1]), 2):
        numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]

print(*numbers)    # Unpacking the list object - *


# Input: 1 2 3 4 5
