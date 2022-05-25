from collections import deque
n, m = map(int, input().split())
maze = []
visit = []

for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(0)
    visit.append(tmp) #미로의 visit판단할 함수

for i in range(n):
    temp = input()
    maze.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(r, c): #bfs 함수
    queue = deque() #큐 선언
    queue.append((r, c)) #큐에 처음 위치 넣어줌
    while queue: #큐가 빌때까지 반복
        y, x = queue.popleft() #큐의 첫번째꺼 꺼냄
        nx = 0 #가위치 
        ny = 0
        for i in range(4): #4방향에 대해 계산
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue #범위 밖 벗어나면 손절
            if int(maze[ny][nx]) == 0: 
                continue #벽 만나면 손절
            if visit[ny][nx] != 0 or (ny, nx) == (0, 0):
                continue #이미 갔던 곳이면 손절, 0,0은 처음값이므로 손절
            #다 통과했을시 해당 위치 까지의 거리는 전 위치까지 거리 +1
            #해당위치에서 또 같은 식의 반복할 것이므로 큐에 넣어줌
            visit[ny][nx] = visit[y][x] + 1
            queue.append((ny, nx)) 

    print(visit[n-1][m-1]+1) 

bfs(0, 0)
#https://www.acmicpc.net/problem/2178

