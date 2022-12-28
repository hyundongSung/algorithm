from sys import stdin

test_case = int(stdin.readline().strip())
numbers = list(map(int, stdin.readline().split()))

v = [1] * (len(numbers))
max_v = 1
for i in range(1, len(numbers)):
    for j in range(i - 1, -1, -1):
        if numbers[i] > numbers[j]:
            v[i] = max(v[i], v[j] + 1)
    max_v = max(max_v, v[i])
    
print(max_v)
