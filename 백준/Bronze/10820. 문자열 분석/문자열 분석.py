from sys import stdin

while True:
    sentence = stdin.readline().rstrip('\n')
    if not sentence:
        break
    cnt = [0] * 4
    for letter in sentence:
        if letter.islower():
            cnt[0] += 1
        elif letter.isupper():
            cnt[1] += 1
        elif letter.isdigit():
            cnt[2] += 1
        elif letter == ' ':
            cnt[3] += 1
    print(' '.join(map(str, cnt)))
