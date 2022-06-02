import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
lablist = []
bfdefault = []
lab = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    lab.append(temp) #기본형 얻기

for i in lab:
    bfdefault += i #bruteforce를 위한 1차원화

flag1, flag2, flag3 = 0, 0, 0
for i in range(n*m):
    for j in range(i+1, n*m):
        for k in range(j+1, n*m):
            flag1, flag2, flag3 = 0, 0, 0 #초기화를 잘해주자....
            dim2 = []
            bf = deque(bfdefault[:])
            if bf[i] == 0:
                bf[i] = 1
                flag1 = 1
            if bf[j] == 0:
                bf[j] = 1
                flag2 = 1
            if bf[k] == 0:
                bf[k] = 1
                flag3 = 1
            
            if flag1+flag2+flag3== 3: #세개 모두 발견했으면 그때 lablist에 추가
                flag1, flag2, flag3 = 0, 0, 0
                for u in range(n):
                    temp = []
                    for v in range(m):
                        temp.append(bf.popleft()) #다시 2차원화 시켜주기
                    dim2.append(temp)
                lablist.append(dim2) #lablist는 3차원 배열로
result = []
for lidx in lablist: #lablist에서 하나씩 꺼내서 bfs진행
    q = deque()
    for i in range(n):
        for j in range(m):
            if lidx[i][j] == 2:
                q.append((i, j)) #bfs시작할점 q에 삽입
    def bfs():
        global result
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if lidx[ny][nx] == 1 or lidx[ny][nx] == 2:
                    continue
                lidx[ny][nx] = 2
                q.append((ny, nx))
        cnt = 0
        for i in range(n):
            for j in range(m):
                if lidx[i][j] == 0:
                    cnt += 1
            
        result.append(cnt)
    bfs()
if len(result) == 0:
    print(0) #모든 경우에대해 bfs진행하고 안전영역없으면 0, 있으면 max값 출력
else:print(max(result)) 
#https://www.acmicpc.net/problem/14502     