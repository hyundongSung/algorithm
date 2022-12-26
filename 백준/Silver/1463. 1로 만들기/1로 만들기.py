import time
from sys import stdin

num = int(stdin.readline())
d = [0] * (num + 1)
d[0] = 1

for i in range(2, num + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        tmp = d[int(i / 2)] + 1
        if tmp < d[i]:
            d[i] = tmp
    if i % 3 == 0:
        tmp = d[int(i / 3)] + 1
        if tmp < d[i]:
            d[i] = tmp

print(d[num])
