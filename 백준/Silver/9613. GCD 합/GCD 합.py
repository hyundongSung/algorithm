from functools import cache
from itertools import combinations
from sys import stdin


@cache
def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


line_num = int(stdin.readline().strip())
for cnt in range(line_num):
    test_case = list(map(int, stdin.readline().strip().split(' ')[1:]))
    result = 0
    for num_a, num_b in list(combinations(test_case, 2)):
        result += gcd(num_a, num_b)
    print(result)
