import sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    pong = sys.stdin.readline().rstrip()
    pong_list = list(pong)
    for i in range(len(pong_list)):
        pong_list[i] = int(pong_list[i])
    board.append(pong_list)

visited = [[0] * N for _ in range(N)] #방문처리할 list

#정석은 함수의 인자로 board와 visited를 재귀내에서 이어주는거
def dfs(r, c, cnt): 
    global board
    global visited
    if r < 0 or r >= N or c < 0 or c >= N:
        return
    if board[r][c] == 0 or visited[r][c] > 0:
        return
    else:
        visited[r][c] = cnt #단지마다 cnt값으로 visited 리스트에 매겨줌
        dfs(r+1, c, cnt)
        dfs(r, c+1, cnt)
        dfs(r-1, c, cnt)
        dfs(r, c-1, cnt)

cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0: #단지상에 1로 존재하고 방문하지않았다면,
            cnt += 1 
            dfs(i, j, cnt)

complex_dict = {} #단지 별 아파트수를 체크하기 위한 딕셔너리
for i in range(N):
    for j in range(N):
        if visited[i][j] > 0:
            try: complex_dict[visited[i][j]] += 1 #있으면 +1
            except: complex_dict[visited[i][j]] = 1 #없으면 단지 이름 key, 단지 아파트 수를 value값으로 추가

print(cnt)
l = list(complex_dict.values())
l.sort()
for i in l:
    print(i)