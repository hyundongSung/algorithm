from sys import stdin

length = int(stdin.readline().strip())
numbers = list(map(int, stdin.readline().split(' ')))

acc = [0] * len(numbers)
acc[0] = numbers[0]
for i in range(1, length):
    if acc[i - 1] > 0:
        acc[i] = acc[i - 1] + numbers[i]
    else:
        acc[i] = numbers[i]
print(max(acc))