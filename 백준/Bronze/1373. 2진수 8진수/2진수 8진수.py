from sys import stdin
from collections import deque

binary = list(map(int, stdin.readline().strip()))
oct_deq = deque()

while binary:
    bin_stack = []
    oct_num = 0
    for cnt in range(3):
        if not binary:
            break
        bin_stack.append(binary.pop())
    for cnt in range(len(bin_stack) - 1, -1, -1):
        oct_num += bin_stack.pop() * (2 ** cnt)
    oct_deq.appendleft(oct_num)

print(''.join(map(str, oct_deq)))
