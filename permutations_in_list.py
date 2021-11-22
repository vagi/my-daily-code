numbers = [int(num) for num in input().split()]
if len(numbers) % 2 == 0:
    for idx in range(0, len(numbers), 2):
        numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
else:
    for idx in range(0, len(numbers[:-1]), 2):
        numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]

print(numbers)
