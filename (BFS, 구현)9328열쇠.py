import sys
from collections import deque
testcase = int(sys.stdin.readline().rstrip())

def bfs(x, y, money_box):
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * m for _ in range(n)]
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == False:
                    
                    if arr[nx][ny] == '.':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif arr[nx][ny] == '*':
                        continue
                    elif arr[nx][ny] == '$':
                        money_box += 1
                        visited[nx][ny] = True
                        arr[nx][ny] = '.'
                        queue.append((nx, ny))
                    else:
                        if arr[nx][ny].islower():
                            keylist.append(arr[nx][ny])
                            visited = [[False] * m for _ in range(n)]
                            visited[nx][ny] = True
                            arr[nx][ny] = '.'
                            queue.append((nx, ny))
                        elif arr[nx][ny].isupper():
                            if arr[nx][ny].lower() in keylist:
                                arr[nx][ny] = '.'
                                visited[nx][ny] = True
                                queue.append((nx, ny))
    return money_box, visited

res = []
                    
for _ in range(testcase):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for i in range(n):
        arr.append(list(sys.stdin.readline().rstrip()))
    keylist = list(sys.stdin.readline().rstrip())

    visited = [[False] * m for _ in range(n)]
    money_box = 0
    pre_money = 0
    #### bfs 시작부터 찾는 경우도 생각 해 줘야 함 ####
    while True:
        for i in range(n):
            for j in range(m):
                if i == n-1 or j == m-1 or i == 0 or j == 0:
                    if visited[i][j] == False:
                        if arr[i][j] == '.':
                            money_box, visited = bfs(i, j, money_box)
                        elif arr[i][j] == '$':
                            money_box += 1
                            money_box, visited = bfs(i, j, money_box)
                            arr[i][j] = '.'
                        elif arr[i][j] == '*':
                            continue
                        else:
                            if arr[i][j].isupper():
                                if arr[i][j].lower() in keylist:
                                    arr[i][j] = '.'
                                    money_box, visited = bfs(i, j, money_box)
                            elif arr[i][j].islower():
                                keylist.append(arr[i][j])
                                arr[i][j] = '.'
                                money_box, visited = bfs(i, j, money_box)
        ###한번 돌고 못찾는 경우가 있을 수 있어서 ###
        if pre_money == money_box:
            break
        pre_money = money_box
    res.append(money_box)

for i in res:
    print(i)