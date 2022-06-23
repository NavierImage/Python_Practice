import sys
sys.setrecursionlimit(10**8)
n, m, k = map(int, sys.stdin.readline().rstrip().split())
road = [[0] * m for _ in range(n)]
for _ in range(k):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    y -= 1
    x -= 1
    road[y][x] = 2

visitcnt = 0
def dfs(r, c):
    global visitcnt
    if r == -1 or r == n or c == -1 or c == m:
        return
    if road[r][c] == 0:
        return
    if road[r][c] == 2:
        visitcnt += 1
        road[r][c] = 0
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
vimax = 0
for i in range(n):
    for j in range(m):
        if road[i][j] == 2:
            visitcnt = 0
            dfs(i, j)
            if vimax < visitcnt:
                vimax = visitcnt
print(vimax)
#https://www.acmicpc.net/problem/1743