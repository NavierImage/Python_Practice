from collections import deque
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
world = []
for _ in range(n):
    world.append(list(map(int, sys.stdin.readline().rstrip().split())))
#copy를 하지 않는게 핵심
#copy가 생각보다 시간이 매우 많이 걸리는 과정....
def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    while queue:
        r, c = queue.popleft()
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if world[nr][nc] != 0 and visited[nr][nc] == 0:
                    #무조건적으로 continue박지 말기...
                    #처음 벗어나는 조건에 대해서 만 해주거나
                    #사실 그마저도 안하고 확실히 명시해주는것이 낫다
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                elif world[nr][nc] == 0:
                    count_water[r][c] += 1

    return 1

year = 0
while True:
    result = []
    visited= [[0] * m for _ in range(n)]
    count_water = [[0] * m for _ in range(n)]
    #bfs가 몇번 수행되는지를 판단하면됨.(여러개 할 필요가 없음)
    #끊어진 곳은 bfs가 수행되지 않을 것이고, 
    #return 값이 하나 더 나올 것임.
    for i in range(n):
        for j in range(m):
            if world[i][j] != 0 and visited[i][j] == 0:
                result.append(bfs(i, j))
    
    #간단한 연산으로 해결가능했는데....
    #세주는 문제 -> 세어진 값들을 저장하는 같은 차원의 배열 만들기
    #마스킹 개념과 비슷.. 
    for i in range(n):
        for j in range(m):
            world[i][j] -= count_water[i][j]
            if world[i][j] < 0:
                world[i][j] = 0
    
    if len(result) >= 2:
        print(year)
        quit()
        
    elif len(result) == 0:
        print(0)
        quit()
    else:
        year += 1
#https://www.acmicpc.net/problem/2573
