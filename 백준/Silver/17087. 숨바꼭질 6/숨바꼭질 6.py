from functools import cache
from sys import stdin


@cache
def gcd(num_a, num_b):
    while num_b != 0:
        tmp = num_b
        num_b = num_a % num_b
        num_a = tmp
    return num_a


bro_num, sub_pos = map(int, stdin.readline().strip().split(' '))
bro_pos = list(map(int, stdin.readline().split(' ')))
distance = [abs(pos - sub_pos) for pos in bro_pos]

cur_gcd = distance[0]
for idx in range(1, len(distance)):
    cur_gcd = gcd(cur_gcd, distance[idx])
    idx += 1

print(cur_gcd)
