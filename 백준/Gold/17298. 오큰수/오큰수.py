import sys

length = int(sys.stdin.readline().strip())
seq = [int(i) for i in sys.stdin.readline().strip().split(' ')]
result = [-1 for time in range(length)]
stack = []

for idx in range(length):
    while stack and seq[idx] > seq[stack[-1]]:
        result[stack[-1]] = seq[idx]
        stack.pop()
        continue
    stack.append(idx)

print(' '.join(map(str, result)))
