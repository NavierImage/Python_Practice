import sys 
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(temp)

S, Y, X = map(int, sys.stdin.readline().rstrip().split())
X -= 1; Y -= 1

vir_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            vir_list.append((i, j, arr[i][j]))
vir_list.sort(key=lambda x:x[2]) #순서 맞추기

def bfs(vir_list):
    queue = deque()
    sec = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(len(vir_list)):
        queue.append((vir_list[i][0], vir_list[i][1], vir_list[i][2], sec))
        visited[vir_list[i][0]][vir_list[i][1]] = 1
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    while queue:
        # print()
        # for a in arr:
        #     print(*a)
        # print()
        y, x, virus, sec = queue.popleft()
        if sec == S:
            return None
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx] == 0:
                    
                    arr[ny][nx] = arr[y][x]
                    visited[ny][nx] = 1
                    queue.append((ny, nx, virus, sec+1))
# print(vir_list)
bfs(vir_list)
print(arr[Y][X])

