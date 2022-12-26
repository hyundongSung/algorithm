from sys import stdin

word = stdin.readline()
result = [0] * 26

for i in range(26):
    for j in range(len(word)):
        if ord(word[j]) == ord('a') + i:
            result[i] += 1
print(' '.join(map(str,result)))
