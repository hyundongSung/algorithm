from collections import deque
import sys

queue = deque()
command_num = int(sys.stdin.readline().strip())
for cnt in range(command_num):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push_front":
        queue.appendleft(int(command[1]))
    elif command[0] == "push_back":
        queue.append(int(command[1]))
    elif command[0] == "pop_front":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
        
