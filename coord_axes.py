"""
Task is here: https://stepik.org/lesson/415554/step/1?unit=405083
first_quarter =  x > 0, y > 0
second_quarter = x < 0, y > 0
third_quarter =  x < 0, y < 0
fourth_quarter = x > 0, y < 0
"""

total = int(input())
coordinates = []
quarters = {1: 0, 2: 0, 3: 0, 4: 0}
for item in range(total):
    coordinates.append([int(i) for i in input().split()])

for idx in coordinates:
    if idx[0] > 0 and idx[1] > 0:
        quarters[1] += 1
    elif idx[0] < 0 and idx[1] > 0:
        quarters[2] += 1
    elif idx[0] < 0 and idx[1] < 0:
        quarters[3] += 1
    elif idx[0] > 0 and idx[1] < 0:
        quarters[4] += 1
print(coordinates)
print(quarters)
print(f"Первая четверть: {quarters[1]}\nВторая четверть: {quarters[2]}\n"
      f"Третья четверть: {quarters[3]}\nЧетвертая четверть: {quarters[4]}")
