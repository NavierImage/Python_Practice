from collections import deque
m, n = map(int, input().split())
tomato = []
for i in range(n):
    temp = list(map(int, input().split()))
    tomato.append(temp)

#동시시작에 대한 구현법이 생각이 안났었다
#시작점을 큐에 넣고시작하면된다!!!!! 개꿀 ㅋㅋ
queue = deque()
visited = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))
#이런식으로 해야 여러곳 시작 가능... 
def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        y, x = queue.popleft()
        ny = 0
        nx = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if tomato[ny][nx] == -1 or tomato[ny][nx] == 1:
                continue
            if visited[ny][nx] >= 1:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))
bfs() #외부에서 큐에 이미 값을 다 넣었기때문에... 사실 굳이 함수 안써도될듯하다
res = []
for i in visited: #visited를 썼기때문에... 문제 발생 ㅜㅜ
    res.append(max(i))
flag = 0
for i in range(len(visited)): #방문을 하지않은곳이 막혀있어서 못간건지 아니면 이미 토마토가 있어서 못간건지를 구분해야함!
    for j in range(len(visited[i])):
        if visited[i][j] == 0: #못간곳인데
            if tomato[i][j] == 0: #토마토가 없는 곳이라면 막혀있어서 못간거임
                flag = 1 #깃발세워주고
                break
            else:
                pass
if flag:
    print(-1) #깃발 서있으면 -1출력
if flag == 0:
    print(max(res)) #아닐경우 최단 거리값을 출력!
#https://www.acmicpc.net/problem/7576