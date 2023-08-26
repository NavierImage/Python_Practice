import sys
from collections import deque
n, m, T = map(int, sys.stdin.readline().rstrip().split())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

def bfs(y, x):
    queue = deque()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    #검 집은 상태와집지않은상태
    visited = [[[0 for col in range(2)] for row in range(m)] for depth in range(n)]
    visited[y][x][0] = 1
    g = 0
    t = 0
    queue.append((y, x, g, t))
    while queue:
        y, x, g, t = queue.popleft()
        if y == n-1 and x == m-1:
            return t 
        
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if g == 0:
                    if visited[ny][nx][g] == 0:
                        if arr[ny][nx] == 0:
                            visited[ny][nx][g] = 1
                            queue.append((ny, nx, g, t+1))
                
                        if arr[ny][nx] == 2:
                            #여기서 g를 건들면 for문 돌면서 다음 턴에 밑의 else if 문에 걸릴 수있음.
                            visited[ny][nx][g+1] = 1
                            queue.append((ny, nx, g+1, t+1))
                elif g == 1:
                    if visited[ny][nx][g] == 0:
                        visited[ny][nx][g] = 1
                        queue.append((ny, nx, g, t+1))
    return None

ans = bfs(0, 0)

if ans == None or ans > T:
    print("Fail")
else:
    print(ans)