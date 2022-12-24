import sys

word = sys.stdin.readline().strip()
stack = []
tag_zone = False

for letter in word:
    if letter == '<':
        tag_zone = True
    if not (tag_zone or letter == ' '):
        stack.append(letter)
        continue
    if stack:
        for cnt in range(len(stack)):
            print(stack.pop(), end='')
    print(letter, end='')
    if letter == '>':
        tag_zone = False

if stack:
    for cnt in range(len(stack)):
        print(stack.pop(), end='')
