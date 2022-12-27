from sys import stdin

card_num = int(stdin.readline().strip())
p = [0] + list(map(int, stdin.readline().split(' ')))
d = [0] * (card_num + 1)

for i in range(1, card_num + 1):
    for j in range(1, i + 1):
        tmp = p[j] + d[i - j]
        if tmp > d[i]:
            d[i] = tmp

print(d[card_num])
