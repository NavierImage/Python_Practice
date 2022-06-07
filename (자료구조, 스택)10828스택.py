import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
stk = deque()
for _ in range(n):
    comd = sys.stdin.readline().rstrip()
    if ' ' in comd:
        lis = comd.split(' ')
        stk.appendleft(int(lis[1]))
    elif comd == 'pop':
        if len(stk) != 0:
            print(stk.popleft())
        else:print(-1)
    elif comd == 'size':
        print(len(stk))
    elif comd == 'empty':
        if len(stk) == 0:
            print(1)
        else:print(0)
    elif comd == 'top':
        if len(stk) != 0:
            print(stk[0])
        else:print(-1)
#https://www.acmicpc.net/problem/10828
#기본 스택
