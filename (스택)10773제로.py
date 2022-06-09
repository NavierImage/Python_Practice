import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
stk = deque()
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        stk.pop()
    else:stk.append(n)
result = 0
for _ in range(len(stk)):
    result += stk.pop()
print(result)
#https://www.acmicpc.net/problem/10773