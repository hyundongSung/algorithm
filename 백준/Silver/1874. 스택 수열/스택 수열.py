length = int(input())
stack = [0]
result = []
cur_num = 1

for counter in range(length):
    target = int(input())
    if target > stack[-1]:
        while cur_num <= target:
            stack.append(cur_num)
            result.append('+')
            cur_num += 1
    if stack[-1] > target:
        break
    stack.pop()
    result.append('-')

if len(result)<2*length:
    print('NO')
else:
    print('\n'.join(result))