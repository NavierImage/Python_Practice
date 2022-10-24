import sys
n = int(sys.stdin.readline().rstrip())
arr = [[0] * (n+4), [0] * (n+4)]
for _ in range(n):
    temp = [0, 0]
    temp.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    temp.extend([0, 0])
    arr.append(temp)
for i in range(2):
    arr.append([0]*(n+4))

y, x = n//2+2, n//2+2
coeff = 0
cnt = 0
##토네이도 모듈 4개, 각 방향별##
def tornado1(u, v):
    du = [-1, 1, -1, 1]
    dv = [-1, -1, 1, 1]
    cache = 0
    for i in range(u-2, u+3):
        if i == u-2 or i == u+2:
            arr[i][v] += int(arr[u][v] * 0.02)
            cache += int(arr[u][v] * 0.02)
        elif i == u+1 or i == u-1:
            arr[i][v] += int(arr[u][v] * 0.07)
            cache += int(arr[u][v] * 0.07)
        elif i == u:
            continue
    for i in range(4):
        if i < 2:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] * 0.1)
            cache += int(arr[u][v] * 0.1)
        else:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] *0.01)
            cache += int(arr[u][v] *0.01)
    arr[u][v-2] += int(arr[u][v] * 0.05)
    cache += int(arr[u][v] * 0.05)
    alpha = arr[u][v] - cache
    arr[u][v] -= (alpha + cache)
    arr[u][v-1] += alpha

def tornado2(u, v):
    du = [1, 1, -1, -1]
    dv = [-1, 1, 1, -1]
    cache = 0
    for j in range(v-2, v+3):
        if j == v-2 or j == v+2:
            arr[u][j] += int(arr[u][v] * 0.02)
            cache += int(arr[u][v] * 0.02)
        elif j == v-1 or j == v+1:
            arr[u][j] += int(arr[u][v] * 0.07)
            cache += int(arr[u][v] * 0.07)
        elif j == v:
            continue
    for i in range(4):
        if i < 2:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] * 0.1)
            cache += int(arr[u][v] * 0.1)
        else:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] * 0.01)
            cache += int(arr[u][v] * 0.01)
    
    arr[u+2][v] += int(arr[u][v] * 0.05)
    cache += int(arr[u][v] * 0.05)
    alpha = arr[u][v] - cache
    arr[u][v] -= (alpha + cache)
    arr[u+1][v] += alpha

def tornado3(u, v):
    du = [-1, 1, -1, 1]
    dv = [1, 1, -1, -1]
    cache = 0
    for i in range(u-2, u+3):
        if i == u-2 or i == u+2:
            arr[i][v] += int(arr[u][v] * 0.02)
            cache += int(arr[u][v] * 0.02)
        elif i == u+1 or i == u-1:
            arr[i][v] += int(arr[u][v] * 0.07)
            cache += int(arr[u][v] * 0.07)
        elif i == u:
            continue
    for i in range(4):
        if i < 2:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] * 0.1)
            cache += int(arr[u][v] * 0.1)
        else:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] *0.01)
            cache += int(arr[u][v] *0.01)
    arr[u][v+2] += int(arr[u][v] * 0.05)
    cache += int(arr[u][v] * 0.05)
    alpha = arr[u][v] - cache
    arr[u][v] -= (alpha + cache)
    arr[u][v+1] += alpha

def tornado4(u, v):
    du = [-1, -1, 1, 1]
    dv = [-1, 1, 1, -1]
    cache = 0
    for j in range(v-2, v+3):
        if j == v-2 or j == v+2:
            arr[u][j] += int(arr[u][v] * 0.02)
            cache += int(arr[u][v] * 0.02)
        elif j == v-1 or j == v+1:
            arr[u][j] += int(arr[u][v] * 0.07)
            cache += int(arr[u][v] * 0.07)
        elif j == v:
            continue
    for i in range(4):
        if i < 2:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] * 0.1)
            cache += int(arr[u][v] * 0.1)
        else:
            arr[u+du[i]][v+dv[i]] += int(arr[u][v] * 0.01)
            cache += int(arr[u][v] * 0.01)
    arr[u-2][v] += int(arr[u][v] * 0.05)
    cache += int(arr[u][v] * 0.05)
    alpha = arr[u][v] - cache
    arr[u][v] -= (alpha + cache)
    arr[u-1][v] += alpha

##단위 나누어서 달팽이모양으로 이동##
for turn in range((len(arr)-4)//2):
    coeff += 1
    ###1
    to_y = y
    to_x = x - (2*coeff-1)
    
    for j in range(x, to_x-1, -1):
        if j == x:
            continue
        tornado1(y, j)

    x = to_x
    y = to_y
    ###2
    to_y = y + (2*coeff-1)
    to_x = x
    for i in range(y, to_y+1):
        if i == y:
            continue
        tornado2(i, x)
    y = to_y
    x = to_x
    
    
    ###3
    to_y = y
    to_x = x + 2*coeff
    for j in range(x, to_x+1):
        if j == x:
            continue
        tornado3(y, j)
    y = to_y
    x = to_x
    
    ###4
    to_y = y - 2*coeff
    to_x = x
    for i in range(y, to_y-1, -1):
        if i == y:
            continue
        tornado4(i, x)
    
    y = to_y
    x = to_x

to_y = y
to_x = x - (2*coeff)
##마지막 이동부분##
for j in range(x, to_x-1, -1):
    tornado1(y, j)
##격자 바깥부분의 합계산##
s = 0
s += sum(arr[0])
s += sum(arr[1])
s += sum(arr[-1])
s += sum(arr[-2])
for i in range(2, len(arr)-2):
    s += arr[i][0]
    s += arr[i][1]
    s += arr[i][len(arr)-1]
    s += arr[i][len(arr)-2] 

print(s)