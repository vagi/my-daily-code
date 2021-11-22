# https://stepik.org/lesson/415554/step/2?unit=405083

numbers = [int(num) for num in input().split()]
counter = 0
for idx in range(1, len(numbers)):
    if numbers[idx] > numbers[idx - 1]:
        counter += 1

print(counter)

# Input: 1 6 2 4 6 7 3 4 5 8 7

# # Firts try - less optimized
# numbers = [int(num) for num in input().split()]
# counter = 0
# idx = 1
# while idx < len(numbers):
#     if numbers[idx] > numbers[idx-1]:
#         counter += 1
#     idx += 1
#
# print(counter)
