from sys import stdin

val = int(stdin.readline())
cnt = 0

for num in range(0, val + 1, 5):
    if num == 0:
        continue
    while num % 5 == 0:
        num /= 5
        cnt += 1

print(cnt)
