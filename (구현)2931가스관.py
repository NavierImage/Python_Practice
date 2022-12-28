import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1] #북 서 남 동
block = ['|', '-', '1', '2', '3', '4', '+', 'M', 'Z']
ans_list = []
whe_list = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == '|':
            for k in [1, -1]:
                ni = i + k
                nj = j
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] not in block:
                        ans_list.append((i, j))
                        whe_list.append((ni, nj))
        elif arr[i][j] == '-':
            for k in [1, -1]:
                ni = i
                nj = j + k
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] not in block:
                        ans_list.append((i, j))
                        whe_list.append((ni, nj))
        elif arr[i][j] == '+':
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] not in block:
                        ans_list.append((i, j))
                        whe_list.append((ni, nj))
        elif arr[i][j] == '1':
            for k in range(2, 4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] not in block:
                        ans_list.append((i, j))
                        whe_list.append((ni, nj))
        elif arr[i][j] == '2':
            for k in range(0, 4, 3):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] not in block:
                        ans_list.append((i, j))
                        whe_list.append((ni, nj))
        elif arr[i][j] == '3':
            for k in range(0, 2):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] not in block:
                        ans_list.append((i, j))
                        whe_list.append((ni, nj))
        elif arr[i][j] == '4':
            for k in range(1, 3):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] not in block:
                        ans_list.append((i, j))
                        whe_list.append((ni, nj))
        elif arr[i][j] == 'M':
            done = 0
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] in block:
                        done = 1
                        break
                
            if done == 0:
                ans_list.append((i, j))
                whe_list.append((-1, -1))
        elif arr[i][j] == 'Z':
            done = 0
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<m:
                    if arr[ni][nj] in block:
                        done = 1
                        break
                
            if done == 0:
                ans_list.append((i, j))
                whe_list.append((-1, -1))

ans_list.sort(key=lambda x:(x[0], x[1]))
i1, j1 = ans_list[0]
i2, j2 = ans_list[1]
hacked = whe_list[0]

a = i1- i2
b = j1- j2

need = ''
if len(ans_list) == 4:
    need = '+'
elif (a, b) == (2, 0) or (a, b) == (-2, 0):
    need = '|'
elif (a, b) == (0, 2) or (a, b) == (0, -2):
    need = '-'
elif (a, b) == (-1, 1) or (a, b) == (1, -1):
    i, j = hacked
    if i == ans_list[0][0]:
        need = '1'
    elif i == ans_list[1][0]:
        need = '3'
elif (a, b) == (1, 1) or (a, b) == (-1, -1):
    i, j = hacked
    if i != ans_list[0][0]:
        need = '2'
    elif i == ans_list[0][0]:
        need = '4'

#########이부분 다시해야함############
for i, whe in enumerate(whe_list):
    ans1, ans2 = whe
if (ans1, ans2) == (-1, -1):
    ans1, ans2 = (i1+i2)//2, (j1+j2)//2
ans1 += 1;ans2 += 1
print(ans1, ans2, need)

