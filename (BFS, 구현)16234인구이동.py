import sys
from collections import deque
n, l, r = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
def bfs(x, y):
    xst, yst = x, y
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    p_list = []
    co_list = []
    p_list.append(arr[x][y])
    co_list.append((x, y))
    visited[x][y] = 1
    queue.append((x, y))
    switch = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == 0 and l<=abs(arr[x][y] - arr[nx][ny])<=r:
                    visited[nx][ny] = 1
                    p_list.append(arr[nx][ny])
                    co_list.append((nx, ny))
                    queue.append((nx, ny))
    if len(p_list)>1:
        switch = 1
        s = sum(p_list)
        mean = int(s/len(p_list))
        for i in range(len(co_list)):
            x, y = co_list[i]
            arr[x][y] = mean
    else:  #아무것도 못했으면 visit한 곳 visit 안했다고 해야함 (visit을 전역변수로 사용할 것이기에)
        visited[xst][yst] = 0
    return switch 
cnt =0 
for k in range(2001):
    visited = [[0] * n for _ in range(n)]
    done = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                switch = bfs(i, j)
                if switch == 1:
                    done = 1
    if done == 0:
        break
    cnt += 1
print(cnt)