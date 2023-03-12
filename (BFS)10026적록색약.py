import sys
from collections import deque 

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

visited1 = [[0] * n for _ in range(n)]
def bfs(y, x):
    queue1 = deque()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited1[y][x] = 1
    queue1.append((y, x))
    pivot = arr[y][x] 
    
    while queue1:
        y, x = queue1.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx <n:
                if pivot == arr[ny][nx]:
                    if visited1[ny][nx] == 0:
                        visited1[ny][nx] = 1
                        queue1.append((ny, nx))

visited2 = [[0] * n for _ in range(n)]
def bfs_rg(y, x):
    queue2 = deque()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited2[y][x] = 1
    queue2.append((y, x))
    if arr[y][x] == "R" or arr[y][x] =="G":
        pivot = ["R", "G"]
    else:
        pivot = ["B"]
    while queue2:
        y, x = queue2.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx <n:
                if arr[ny][nx] in pivot:
                    if visited2[ny][nx] == 0:
                        visited2[ny][nx] = 1
                        queue2.append((ny, nx))

cnt_normal = 0
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs(i, j)
            cnt_normal += 1
cnt_abnormal = 0
for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            bfs_rg(i, j)
            cnt_abnormal += 1
print(cnt_normal, cnt_abnormal)