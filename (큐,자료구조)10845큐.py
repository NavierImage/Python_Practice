import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
disp = []
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if ' ' in command:
        c = command.split(' ')
        queue.append(int(c[1]))
    elif command == 'pop':
        if len(queue) != 0:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    elif command == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
        
    elif command == 'size':
        print(len(queue))
    
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else: print(0)
    elif command == 'back':
        if len(queue) != 0:
            print(queue[len(queue) -1])
        else:
            print(-1)
