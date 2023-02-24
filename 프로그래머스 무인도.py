from collections import deque 
def bfs(y, x, arr, visited):
    queue = deque()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    n = len(arr)
    m = len(arr[0])
    
    queue.append((y, x))
    total = int(arr[y][x])
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == 0:
                    if arr[ny][nx] != "X":
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        total += int(arr[ny][nx])
    return visited, total

def solution(maps):
    arr = []
    for temp in maps:
        arr.append(list(temp))
    n = len(arr)
    m = len(arr[0])
    visited = [[0] * m for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 'X' and visited[i][j] != 1:
                visited, total = bfs(i, j, arr, visited)
                answer.append(total)
    if answer == []:
        answer.append(-1)
    return answer

solution(["XXX","XXX","XXX"])
