import sys


n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

cnt = 0

def dfs(y, x, status):
    global cnt 
    if y < 0 or y >= n or x < 0 or x >= n:
        return 

    if x == n-1 and y == n-1:
        cnt += 1
        return 

    if 0<=y+1<n and 0<=x+1<n:
        if arr[y+1][x+1] != 1 and arr[y][x+1] != 1 and arr[y+1][x] != 1:
            dfs(y+1, x+1, 2) #대각선인 경우

    if status == 0 or status == 2: #가로 
        if 0<=y<n and 0<=x+1<n:
            if arr[y][x+1] != 1:
                dfs(y, x+1, 0) #가로인 경우
        
    if status == 1 or status == 2:
        if 0<=y+1<n and 0<=x<n:
            if arr[y+1][x] != 1:
                dfs(y+1, x, 1) #세로인 경우

dfs(0, 1, 0)
print(cnt)