import sys
from collections import deque
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
inner_visited = [[0] * n for _ in range(n)]
def inner_bfs(r, c, counter):
    contour_points = []
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    inner_queue = deque()
    inner_queue.append((r, c))
    inner_visited[r][c] = counter
    while inner_queue:
        r, c = inner_queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc < n:
                if board[nr][nc] == 1 and inner_visited[nr][nc] == 0:
                    inner_queue.append((nr, nc))
                    inner_visited[nr][nc] = counter
                elif board[nr][nc] == 0:
                    contour_points.append((nr, nc))

    return contour_points

total_contour_points = []
counter = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and inner_visited[i][j] == 0:
            #발견한 순서대로 순서 지정(counter 변수)
            counter += 1 
            contour_points = inner_bfs(i, j, counter)
            if len(contour_points) > 0:
                total_contour_points.append(contour_points)

def outer_bfs(r, c, instance):
    outer_visited = [[0] * n for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    queue.append((r, c))
    outer_visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc < n:
                if inner_visited[nr][nc] == instance:
                    continue
                    
                elif inner_visited[nr][nc] != instance and outer_visited[nr][nc] == 0:
                    if board[nr][nc] == 0:
                        queue.append((nr, nc))
                        outer_visited[nr][nc] = outer_visited[r][c] + 1
                    elif board[nr][nc] == 1:
                        return outer_visited[r][c]
    return -1
results = []
for i in range(len(total_contour_points)):
    for j in range(len(total_contour_points[i])):
        a, b = total_contour_points[i][j]
        #innerbfs진행하며 지정해주었던 순서와, total_contour_points에서 검사하는 순서가 일치함.
        #따라서 outer_bfs의 instance는 자기 자신을 검사하지 않게 방지해주는 역할.
        res = outer_bfs(a, b, i+1)
        if res == -1:
            continue
        results.append(res)
print(min(results))
#res = -1로 만드는 이유
#다음 반례(비어있는 섬.) (정답은 3)
#5     
#1 0 0 0 0
#0 0 0 0 0
#0 0 1 1 1
#0 0 1 0 1
#0 0 1 1 1
#ans: 3