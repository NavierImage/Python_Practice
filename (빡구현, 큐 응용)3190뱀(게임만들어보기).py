n = int(input()) 
k = int(input())

board = []
for i in range(n): #보드 만들어주기
    temp = []
    for j in range(n):
        temp.append(0)
    board.append(temp)

for i in range(k):  #보드 상에 사과 위치 만들어 주기
    row, col = map(int, input().split())
    board[row-1][col-1] = 2 

l = int(input())
time = []
dir_change = []
for i in range(l): #방향을 돌릴 시간, 돌릴 방향 설정
    sec, rev =  input().split()
    time.append(int(sec))
    dir_change.append(rev)

x, y = 0, 0
dx = [1, -1, 0, 0]; dy = [0, 0, 1, -1] #동서남북
#디폴트 동쪽
dir = 200 #기본값 200 
#나머지 0 동쪽 나머지 1 남쪽 나머지 2 서쪽 나머지 3 북쪽
body = [[0, 0]] #body리스트에 기본으로 머리 들어가있음
t = 0 #시간 0초에서 시작
while(1):
    t += 1 #시간 1초씩추가
    nx = 0; ny = 0 #가위치

    #나머지값으로 방향을 판단하고 해당 방향으로 진출
    if dir % 4 == 0:
        nx = x + dx[0]; ny = y + dy[0]
    elif dir % 4 == 1:
        nx = x + dx[2]; ny = y + dy[2]
    elif dir % 4 == 2:
        nx = x + dx[1]; ny = y + dy[1]
    elif dir % 4 == 3:
        nx = x + dx[3]; ny = y + dy[3]
    
    #방향 돌릴시간이 됐을때 방향 조절해줌
    if t in time:
        if dir_change[time.index(t)] == 'D': #D면 오른쪽
            dir += 1
        elif dir_change[time.index(t)] == 'L': #L이면 왼쪽 회전
            dir -= 1
    
    if nx >= n or ny >= n or nx < 0 or ny < 0:
        break #벽에 부딫힐 경우 탈출
 
    if [ny, nx] in body: 
        break #자기 몸에 부딫힐 경우 탈출

    if board[ny][nx] == 2: #사과 만나면 늘린머리 유지하기
        board[ny][nx] = 0
        body.append([ny, nx])
    
    else: #사과 없다면 머리 이동후 꼬리 자르기 (큐)
        #ex: [0, 1], [0, 2]에서 한칸 이동하면
        # [0, 2], [0, 3]이 됨 
        # 방향 꺾여도 Data만 잘 가지고 있다면 구현 됨
        body.append([ny, nx])
        body.pop(0)
    
    y, x = ny, nx

print(t)
 
#https://www.acmicpc.net/problem/3190