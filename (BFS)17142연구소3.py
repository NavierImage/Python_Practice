import sys
from collections import deque
from itertools import combinations
n, m = map(int, sys.stdin.readline().rstrip().split())
clab = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    clab.append(temp)

comb = []
blank = 0
for i in range(n):
    for j in range(n):
        if clab[i][j] == 2:
            comb.append((i, j))
        if clab[i][j] == 0:
            blank += 1 #빈칸의 갯수 세주기(빈칸 갯수 변수는, 밑에서도 썼지만 바이러스 가득찬 상황에는 더이상 진행 하지 않아도 되니깐 그것을 판단하는 용으로.)
rst=[]
rblank = blank #반복들어가면 초기화를 못해주니 초기화용 변수 rblank하나 선언
#반복의 시작마다 , 어디서 초기화를 해줘야할지 잘 생각해야함.
for iter in combinations(comb, m):
    blank = rblank #blank초기화
    lab = []
    for u in clab:
        lab.append(u[:])

    visited = [[0] * n for i in range(n)] #여기에 간 시간이 기록됨
    q = deque()
    for j in iter:
        q.append(j)
        r, c = j
        
    for j in comb:
        if j in q:
            continue
        r, c = j
        lab[r][c] = 3
    
    def bfs():
        global blank #bfs함수에서 blank 사용하기위해.
        while q:
            y, x = q.popleft()
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            if blank == 0: #만약 빈칸없다면 컷, 이렇게해야 비활성화 바이러스는 남아있지만 빈칸이 없을때(즉, 활성화, 비활성화의 구분없이 그냥 바이러스로 가득찬 상황)
                break      #전체 감염시간을 판단할 수가 있음.
                           #for 문으로 매번 0의 유무를 판단하여 하였으나 그렇게하면 시간초과남!!!!!

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                
                if lab[ny][nx] == 1 or visited[ny][nx] != 0:
                    continue
                
                if lab[ny][nx] == 0:
                    lab[ny][nx] = 2
                    blank -= 1 #0을 감염시키는건 빈칸을 없애는거니깐 blank -=1 해주기
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                if lab[ny][nx] == 3: #3은 비활성화 바이러스이므로 blank건드리지않는다
                    lab[ny][nx] = 2 
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
    bfs()           
    tp = []
    cnt = 0
    for k in range(n):
        if 0 in lab[k]:
            cnt = 1
            break
        tp.append(max(visited[k]))

    if cnt == 0:
        rst.append(max(tp))
if len(rst)==0:
    print(-1) #예외 케이스 고려, 절대 감염못시키는경우
else:print(min(rst))
