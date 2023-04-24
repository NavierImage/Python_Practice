import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

y, x = map(int, sys.stdin.readline().rstrip().split())
y-=1;x-=1

order_dict = {}
arr = [[0] * n for _ in range(n)]
for order in range(m):
    temp1, temp2 = map(int, sys.stdin.readline().rstrip().split())
    arr[temp1-1][temp2-1] = 1
    order_dict[(temp1-1, temp2-1)] = order

ans_list = []
def bfs(y, x):
    queue = deque()
    cnt = 0
    queue.append((y, x, cnt))
    visited = [[0] * n for _ in range(n)]

    visited[y][x] = 1
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    while queue:
        y, x, cnt = queue.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx] == 0:
                    if arr[ny][nx] == 1:
                        ans_list.append((cnt+1, order_dict[(ny, nx)]))
                        visited[ny][nx] = 1
                        queue.append((ny, nx, cnt + 1))
                    else:
                        visited[ny][nx] = 1
                        queue.append((ny, nx, cnt+1))

bfs(y, x)
ans_list.sort(key = lambda x: x[1])
real_ans = []
for a in ans_list:
    real_ans.append(a[0])
print(*real_ans)
