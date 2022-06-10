import sys
from collections import deque
m, n = map(int, sys.stdin.readline().rstrip().split())
prime = deque()
for i in range(m, n+1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        prime.append(i)

while prime:
    p = prime.popleft()
    if p == 1: continue
    print(p)
#https://www.acmicpc.net/problem/1929
