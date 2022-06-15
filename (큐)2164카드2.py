#https://www.acmicpc.net/problem/2164
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
q = deque()
for i in range(n):
    q.append(i+1)
i = -1
while len(q) != 1:
    i += 1
    if i % 2 == 0:
        q.popleft()
    elif i % 2 == 1:
        q.append(q.popleft())

print(q.popleft())
#간단