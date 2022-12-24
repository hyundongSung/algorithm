import sys

info = sys.stdin.readline().strip()
stack = []
cut = 0

for cur_idx in range(len(info)):
    if info[cur_idx] == '(':
        stack.append(cur_idx)
        continue
    if cur_idx - stack[-1] == 1:
        cut += len(stack) - 1
    else:
        cut += 1
    stack.pop()
print(cut)
