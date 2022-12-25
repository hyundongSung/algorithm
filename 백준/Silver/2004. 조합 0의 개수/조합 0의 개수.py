from sys import stdin
from functools import cache


@cache
def count(val, target):
    cnt = 0
    num = target
    while num <= val:
        cnt += int(val / num)
        num *= target
    return cnt


n, m = map(int, stdin.readline().split(' '))
five_sum = count(n, 5) - count(n - m, 5) - count(m, 5)
two_sum = count(n, 2) - count(n - m, 2) - count(m, 2)
print(min(five_sum, two_sum))