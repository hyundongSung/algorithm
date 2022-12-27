from sys import stdin

num = int(stdin.readline())
d = [[0] * 2 for _ in range(num + 1)]
d[1][1] = 1

for n in range(2, num + 1):
    d[n][0] = d[n - 1][0] + d[n - 1][1]
    d[n][1] = d[n - 1][0]

print(sum(d[num]))
