from sys import stdin
from collections import deque

octal = list(map(int, stdin.readline().strip()))
bin_deq = deque()

while octal:
    init_oct = octal.pop()
    if not octal and init_oct == 0:
        bin_deq.append(0)
        break

    remain_oct = init_oct
    for cnt in range(3):
        if remain_oct == 0 and not octal:
            break
        bin_deq.appendleft(remain_oct % 2)
        remain_oct = int(remain_oct / 2)

print(''.join(map(str, bin_deq)))
