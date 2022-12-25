import math
from sys import stdin

even_number = []
while True:
    val = int(stdin.readline().strip())
    if val == 0:
        break
    even_number.append(val)

min_num = min(even_number)
max_num = max(even_number)
prime = [True for i in range(max_num + 1)]

for factor in range(2, int(math.sqrt(max_num)) + 1):
    if not prime[factor]:
        continue
    mult = factor
    while factor * mult <= max_num:
        prime[factor * mult] = False
        mult += 1

for num in even_number:
    for odd in range(3, num + 1, 2):
        if prime[odd] and prime[num - odd]:
            print(f'{num} = {odd} + {num - odd}')
            break
