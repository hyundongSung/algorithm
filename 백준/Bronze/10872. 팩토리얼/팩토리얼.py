from sys import stdin

val = int(stdin.readline())
result = 1

if val != 0:
    for num in range(val, 0, -1):
        result *= num
print(result)
