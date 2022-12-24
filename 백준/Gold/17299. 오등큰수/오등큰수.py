import sys
from collections import Counter

length = int(sys.stdin.readline().strip())
seq = list(map(int, sys.stdin.readline().split()))
freq = Counter(seq)
result = [-1]*length
stack = []

for idx in range(length):
    while stack:
        cur_num = seq[idx]
        top_num = seq[stack[-1]]
        if freq[cur_num] > freq[top_num]:
            result[stack.pop()] = cur_num
        else:
            break
    stack.append(idx)

print(' '.join(map(str, result)))
