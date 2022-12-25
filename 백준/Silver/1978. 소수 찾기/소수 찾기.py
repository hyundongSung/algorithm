from sys import stdin


def check(num):
    global cnt
    div = 2

    if num == 1:
        return
    while div * div <= num:
        if num % div == 0:
            return
        div += 1
    cnt += 1


total_case = int(stdin.readline().strip())
candidate = list(map(int, stdin.readline().strip().split(' ')))
cnt = 0

for idx in range(total_case):
    check(candidate[idx])
print(cnt)
