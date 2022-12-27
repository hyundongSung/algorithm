from sys import stdin

test_case = int(stdin.readline())
d = [1] * 1_000_001
d[2] = 2
for rep in range(3, 1_000_001):
    d[rep] = (d[rep - 1] + d[rep - 2] + d[rep - 3]) % 1_000_000_009
for cnt in range(test_case):
    num = int(stdin.readline().strip())
    print(d[num])
