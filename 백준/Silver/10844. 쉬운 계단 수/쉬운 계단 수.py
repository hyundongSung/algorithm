from sys import stdin

num = int(stdin.readline())
d = [[0] * 10 for _ in range(num + 1)]
mod = 1000000000

for i in range(10):
    if i > num:
        break
    if i > 1:
        d[i][i] = 1
    if i == 1:
        for j in range(1, 10):
            d[1][j] = 1

for n in range(2, num + 1):
    for k in range(0, 10):
        if k == 0:
            d[n][0] = d[n - 1][1]
            continue
        if k == 9:
            d[n][9] = d[n - 1][8]
            continue
        d[n][k] = d[n - 1][k - 1] + d[n - 1][k + 1]
        d[n][k] %= mod

print(sum(d[num]) % mod)
