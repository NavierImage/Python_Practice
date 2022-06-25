from hashlib import blake2b
import sys
n = int(sys.stdin.readline().rstrip())
favor = []
for _ in range(n**2):
    favor.append(list(map(int ,sys.stdin.readline().rstrip().split())))

board = [[0] * n for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for student in favor:
    adjacent = [[0] * n for _ in range(n)] #인접한 학생을 셀 리스트
    blank = [[0] * n for _ in range(n)] #빈칸을 셀 리스트
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue
            for d in range(4): #주변 check
                ny = i + dy[d]
                nx = j + dx[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[ny][nx] in student[1:]:
                    adjacent[i][j] += 1 #(i, j)의 인접한 좋아하는 사람이 몇명있는지 
                if board[ny][nx] == 0:
                    blank[i][j] += 1 #(i, j)의 인접한 빈칸이 몇개인지

    max_adj = max(map(max, adjacent)) #좋아하는 사람의 최댓값 (2차원에서 가져오기)
    max_blk = max(map(max, blank)) #빈칸의 최댓값
    
    if max_adj == 0: #만약 인접한 좋아하는 사람이 없다면
        flag = 0
        for i in range(n):
            for j in range(n):
                if blank[i][j] == max_blk:
                    if board[i][j] == 0: #그냥 max_adj = 0이고 max_blk = 0인 경우가있어서, 그 경우를 제외시키기 위한것
                        board[i][j] = student[0]
                        flag = 1
                        break
            if flag:
                break
    
    else:
        tempmaxadj = []
        tempmaxblk = []
        for i in range(n):
            for j in range(n):
                if adjacent[i][j] == max_adj: #만약 인접한 좋아하는 사람이 있는 것의 최댓값이 여러개면
                    tempmaxadj.append((i, j)) #추가
        
        for i in range(len(tempmaxadj)):
            r, c = tempmaxadj[i] #그 최댓값 여러개인 곳의 빈칸 정보를 tempmaxblk에 추가
            tempmaxblk.append([r, c, blank[r][c]]) #행, 렬, 주변 빈칸 수

        tempmaxblk.sort(key = lambda x :(-x[2], x[0], x[1])) #정렬 순서: 빈칸 많은 순, 행, 열

        for i in range(len(tempmaxblk)):
            u, v = tempmaxblk[0][0], tempmaxblk[0][1] #위에서 정렬된 결과의 가장 첫째값.
            board[u][v] = student[0]

deter = []
for i in range(len(favor)):
    deter.append(favor[i][0]) #favor[i][0]이 자리배치할 학생. 순서대로 넣은 곳을 deter list에
pls = 0
for i in range(n): #만족도 계산
    for j in range(n):
        idx = deter.index(board[i][j])
        cnt = 0
        for d in range(4):
            ny = i + dy[d]
            nx = j + dx[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[ny][nx] in favor[idx][1:]:
                cnt += 1
                
        if cnt != 0:
            pls += 10**(cnt-1) #만족도 추가

print(pls)
#https://www.acmicpc.net/problem/21608
            