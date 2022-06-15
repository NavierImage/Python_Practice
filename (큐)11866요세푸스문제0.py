#https://www.acmicpc.net/problem/11866
import sys
from collections import deque
n, k = map(int,sys.stdin.readline().rstrip().split())
q = deque()
for i in range(n):
    q.append(i+1)
j = 0
result = []
while q: #queue가 빌때까지 맨앞원소가 대상 원소이면 제거, 아니면 뒤로 보내는식으로 반복
    j += 1
    if j == k:
        j = 0
        result.append(q.popleft())
    else:
        q.append(q.popleft())
print('<', end = '')
for i in range(len(result)-1):
    print('%d,' %result[i], end = ' ')
print('%d>'%result[len(result)-1], end ='')