import sys
from collections import Counter

length = int(sys.stdin.readline().strip())
seq = list(map(int, sys.stdin.readline().split()))
freq = Counter(seq)
result = [-1]*length
stack = []

for idx in range(length):
    cur_num = seq[idx]
    while stack:
        top_num = seq[stack[-1]]
        if freq[cur_num] > freq[top_num]:
            result[stack[-1]] = cur_num
            stack.pop()
            continue
        else:
            break
    stack.append(idx)

print(' '.join(map(str, result)))
