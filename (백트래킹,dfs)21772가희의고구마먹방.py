import sys 
sys.setrecursionlimit(10**4)
N, M, T = map(int, sys.stdin.readline().rstrip().split())
arr = []

for i in range(N):
    arr.append(list(sys.stdin.readline().rstrip()))

visited = [[0] * M for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ans = 0
cnt = 0
def dfs(y, x, time, cnt):
    global ans
    if y < 0 or y >= N or x < 0 or x >= M:
        return
    if arr[y][x] == "#":
        return 
    
    if time > T:
        ans = max(cnt, ans)
        return
 
    checker = 0 ##visited 배열 대신, 이렇게해야 한번 왔던 곳이라도 고구마를 먹고 지나갈 수 있음.
    if arr[y][x] == "S": 
        cnt += 1
        arr[y][x] = "."
        checker = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        dfs(ny, nx, time+1, cnt)
    if checker: # 함수 끝나고, 풀어줄때 원래 고구마 있던 자리면 돌려줘야함.
        arr[y][x] = "S"

for i in range(N):
    for j in range(M):
        if arr[i][j] == "G":
            dfs(i, j, 0, 0)
print(ans)