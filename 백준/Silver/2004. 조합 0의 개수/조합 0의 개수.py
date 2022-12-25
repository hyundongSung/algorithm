from functools import cache
from sys import stdin


@cache
def count(n, m, target):
    cnt = 0
    div = target
    while div <= n:
        cnt += int(n / div)
        div *= target
    div = target
    while div <= n - m:
        cnt -= int((n - m) / div)
        div *= target
    div = target
    while div <= m:
        cnt -= int(m / div)
        div *= target
    return cnt


n, m = map(int, stdin.readline().split(' '))
print(min(count(n, m, 5), count(n, m, 2)))
