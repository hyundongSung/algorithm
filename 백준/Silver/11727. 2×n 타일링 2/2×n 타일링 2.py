from sys import stdin

num = int(stdin.readline())
d = [0] * (num + 1)
d[1] = 1

if num != 1:
    d[2] = 3
    for i in range(3, num + 1):
        d[i] = d[i - 1] + 2*d[i-2]

print(d[num] % 10007)
