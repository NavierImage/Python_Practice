import sys
from collections import deque
tc = int(sys.stdin.readline())
res = []
for iii in range(tc): #테스트케이스
    bd = []
    m, n = map(int, sys.stdin.readline().split())
    visited = [[0] * m for ii in range(n)] #visited리스트 
    for i in range(n):
        bd.append(list(input()))
            
    q = deque()
    fq = deque()

    for i in range(n):
        for j in range(m):
            if bd[i][j] == '@': #상근이의 이동경로 bfs할 queue
                q.append((i, j))
                visited[i][j] = 1
            elif bd[i][j] == '*': #불의 이동경로 bfs할 queue 
                fq.append((i, j))
    
    def bfs():
        global q; global fq #전역변수로
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        flag = 0
        while q: #queue가 빌때까지 
            temp = [] #테크닉 1 - temp 리스트 활용하여 큐를 비워줄때까지, 그리고 다시 채워주기
            while fq:
                y, x = fq.popleft()
                nx = 0; ny = 0
                for p in range(4):
                    nx = x + dx[p]
                    ny = y + dy[p]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if bd[ny][nx] == '#' :
                        continue
                    if bd[ny][nx] == '.':
                        bd[ny][nx] = '*'
                        temp.append((ny, nx))
            
            fq = deque(temp)
            nx = 0; ny = 0
            tmpq = []
            while q: #테크닉 2 - 마찬가지로 tmpqueue리스트를 설정해서, 이전의 q들안에 있던
                #점들에 대해 모두 bfs진행해주고 새로운 tmpqueue에 인접한곳 저장해주고 q로 넘김
                #이렇게 안하면, q에있던거 하나만 뽑고 그냥 다음 반복 횟수로 넘어가게됨
                y, x = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        flag = 1
                        res.append(visited[y][x])
                        break #찾으면 break, flag 세워주기
                    if bd[ny][nx] == '#':
                        continue
                    if bd[ny][nx] == '.' and visited[ny][nx] == 0:
                        bd[ny][nx] = '@'
                        bd[y][x] = '.'
                        visited[ny][nx] = visited[y][x] + 1
                        tmpq.append((ny, nx))
                if flag:
                    break #flag == 1일시
            if flag:
                break #flag == 1일시..
            q = deque(tmpq)
        if flag == 0:
            res.append('IMPOSSIBLE')
    bfs()
for i in res:
    print(i)