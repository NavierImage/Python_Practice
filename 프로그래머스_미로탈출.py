from collections import deque
def bfs(y, x, arr):
    queue =deque()
    n = len(arr)
    m = len(arr[0])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[y][x][0] = 1
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    queue.append((y, x, 0))
    while queue:
        y, x, sta = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == "O":
                    if visited[ny][nx][sta] == 0:
                        visited[ny][nx][sta] = visited[y][x][sta] + 1
                        queue.append((ny, nx, sta))
                elif arr[ny][nx] == "L":
                    if visited[ny][nx][sta] == 0:
                        visited[ny][nx][sta] = visited[y][x][sta] + 1
                        queue.append((ny, nx, sta))
                        if sta == 0:
                            visited[ny][nx][1] = visited[y][x][sta] + 1
                            queue.append((ny, nx, 1))
                elif arr[ny][nx] == "E":
                    if sta == 1:
                        return visited[y][x][sta]
                    else:
                        visited[ny][nx][sta] = visited[y][x][sta] + 1
                        queue.append((ny, nx, sta))
                elif arr[ny][nx] == "S":
                    if visited[ny][nx][sta] == 0:
                        visited[ny][nx][sta] = visited[y][x][sta] + 1
                        queue.append((ny, nx, sta))
    return -1
def solution(maps):
    arr = []
    for i in maps:
        arr.append(list(i))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "S":
                answer = bfs(i, j, arr)
    return answer



