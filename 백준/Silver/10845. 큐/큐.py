from collections import deque
import sys

queue = deque()
command_num = int(sys.stdin.readline().strip())
for cnt in range(command_num):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        queue.append(int(command[1]))
        continue
    if command[0] == "pop":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
        continue
    if command[0] == "size":
        print(len(queue))
        continue
    if command[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)
        continue
    if command[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
        continue
    if command[0] == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
        continue
