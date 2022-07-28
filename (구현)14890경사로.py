import sys
import copy
n, l = map(int, sys.stdin.readline().rstrip().split())

road = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    road.append(temp)
cnt = 0

road_t = [[0] * n for _ in range(n)] #회전된거

for j in range(n):
    for i in range(n):
        road_t[i][j] = road[j][i]

for rotate in range(2):
    visited = [[0] * n for _ in range(n)]

    if rotate == 1: #두번째엔 전치 된 배열로
        road = copy.deepcopy(road_t)

    for i in range(n):
        cantflag = 0
        for j in range(n-1):
            if road[i][j] - road[i][j+1] == 1: #내리막
                for k in range(j+1, j+l+1):
                    if k >= n:
                        cantflag = 1
                        break
                    if road[i][k] != road[i][j+1]:
                        cantflag = 1
                        break
                    if visited[i][k] == 1:
                        cantflag = 1
                        break
                    visited[i][k] =1    
                if cantflag == 1:
                    break
            elif road[i][j] - road[i][j+1] == -1: #오르막
                for k in range(j, j-l, -1):
                    if k < 0:
                        cantflag = 1
                        break
                    if road[i][k] != road[i][j]:
                        cantflag = 1
                        break
                    if visited[i][k] == 1:
                        cantflag = 1
                        break
                    visited[i][k] = 1
                if cantflag == 1:
                    break
            elif road[i][j] == road[i][j+1]:
                pass
            else:
                cantflag = 1
                break
            
            
        if cantflag == 0:
            cnt += 1

 
print(cnt)