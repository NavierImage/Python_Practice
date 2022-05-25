#2468
import sys
sys.setrecursionlimit(10**7)
def dfs(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return False #벽밖컷
    if room[y][x] > rain and room[y][x] != -1:  
        #y행 x열 위치의 값이 빗물보다 높으면 True
        room[y][x] = -1 #방문 처리!
        #순서대로 스택쌓으면서 이어져있는 
        #모든 상하좌우 방향에 대해 재귀적으로 탐색하며 방문처리함
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    else:
        return False #빗물양보다 작으면 컷

n = int(input())
room = []
nroom = []
for i in range(n):
    temp = list(map(int, input().split()))
    room.append(temp)
for i in range(n):
    nroom.append(room[i][:])


rain = 0
result = []
for k in range(102): #빗물의 양 최대가 100이므로... 비효율적이나 그냥 검사
    room = []
    for i_ in range(n):
        room.append(nroom[i_][:])
    rain += 1
    cnt = 0

    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    result.append(cnt)
     
if max(result) == 0:#반례 check
    print(1)
else:
    print(max(result))
#https://www.acmicpc.net/problem/2468

