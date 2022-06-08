import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
deq = deque()
for _ in range(n):
    comd = sys.stdin.readline().rstrip()
    print(comd)
    temp = []
    if 'push_back' in comd:
        temp = comd.split(' ')
        deq.append(int(temp[1]))
    elif 'push_front' in comd:
        temp = comd.split(' ')
        deq.appendleft(int(temp[1]))
    elif comd == 'pop_front':
        if len(deq) != 0:
            print(deq.popleft())/Users/ijeonghwan/vscode/(자료구조, 덱)10866덱.py
        else: print(-1)
    elif comd == 'pop_back':
        if len(deq) != 0:
            print(deq.pop())
        else: print(-1)
    elif comd == 'size':
        print(len(deq))
    elif comd == 'empty':
        if len(deq) == 0:
            print(1)
        else: print(0)
    elif comd == 'front':
        if len(deq) != 0:
            print(deq[0])
        else:print(-1)
    elif comd == 'back':
        if len(deq) != 0:
            print(deq[len(deq)-1])
        else:print(-1)

        
