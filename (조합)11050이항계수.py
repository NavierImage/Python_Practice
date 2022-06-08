import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
res = 1

for i in range(k):
    res *= n
    n -= 1
for i in range(k, 0, -1):
    res /= i

print(int(res))
#https://www.acmicpc.net/problem/11050