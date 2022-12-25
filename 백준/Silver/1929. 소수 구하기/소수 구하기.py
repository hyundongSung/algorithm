import math
from sys import stdin

min_num, max_num = map(int, stdin.readline().split(' '))
prime = [True for i in range(max_num + 1)]

for factor in range(2, int(math.sqrt(max_num)) + 1):
    if not prime[factor]:
        continue
    mult = factor
    while factor * mult <= max_num:
        prime[factor * mult] = False
        mult += 1

for num in range(min_num, max_num + 1):
    if num != 1 and prime[num]:
        print(num)
