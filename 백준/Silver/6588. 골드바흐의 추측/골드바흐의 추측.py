import math
from sys import stdin

even_number = []
while True:
    val = int(stdin.readline().strip())
    if val == 0:
        break
    even_number.append(val)

max_num = max(even_number)
prime = [True for cnt in range(max_num + 1)]

for factor in range(2, int(math.sqrt(max_num)) + 1):
    if prime[factor]:
        for non_prime in range(factor ** 2, max_num, factor):
            prime[non_prime] = False

for num in even_number:
    for odd in range(3, num + 1, 2):
        if prime[odd] and prime[num - odd]:
            print(f'{num} = {odd} + {num - odd}')
            break
