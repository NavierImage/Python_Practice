import sys
from collections import deque
from itertools import combinations #조합 사용할 것이라서 ㅋㅋ
n, m = map(int, sys.stdin.readline().split())
lab = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    lab.append(temp)
comb = []
queue = deque()
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            comb.append((i, j)) 
res = []

def bfs():
    brcnt = 0
    cnt = 0
    for i in combinations(comb, m): #comb리스트에 대해 조합이용
        cnt += 1
        visited = [[0]*n for p in range(n)]
        stpoint = [] #엣지케이스 방지를 위해 시작 포인트들을 다 저장
        for j in i:
            stpoint.append(j) 
            queue.append(j) #시작할 포인트들을 큐에 삽입
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while queue:
            y, x = queue.popleft()
            ny = 0
            nx = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if lab[ny][nx] == 1:
                    continue
                if visited[ny][nx] != 0:
                    continue
                #시작점의 visited값이 0이라 bfs돌리면 다시 뒤를 찾아가는 경우가있음. 그걸 방지해야
                if (ny, nx) in stpoint: #이거 엣지케이스인데 ... 그냥 대충 넘어가지말자 ㅜㅜ
                    continue
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
        flag = 0
        tmp = []
        for u in range(n):
            tmp.append(max(visited[u]))
            for v in range(n):
                if visited[u][v] == 0: 
                    #visited와 lab간의 값 비교하여 visited 값 0인곳에 대해
                    #벽인지, 방문한곳인지, 시작점인지를 check
                    if lab[u][v] == 1 or (u, v) in stpoint:
                        pass
                    else:
                        flag = 1
                        break
                if flag == 1:
                    break
        if flag == 1:
            brcnt += 1 #만약 방문 못한곳이 있다면 brcnt 1 올려줌
        else:
            res.append(max(tmp)) #i번경우에 대한 최단 경로값 res리스트에 추가

    if brcnt == cnt: #모든 튜플 조합들에 대해 다 진행했는데 올려진 brcnt 수가 조합의 수인 cnt와 같다면 -1출력
        print(-1)
    else:
        print(min(res)) #모두 감염 시킨 case가있다면 최단경로가 가장 작은 경우를 출력   
              
bfs()
#https://www.acmicpc.net/problem/17141