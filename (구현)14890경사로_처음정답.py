import sys
n, l = map(int, sys.stdin.readline().rstrip().split())

road = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    road.append(temp)
cnt = 0

visited = [[0] * n for _ in range(n)]
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

visited = [[0] * n for _ in range(n)]
for j in range(n):
    cantflag = 0
    for i in range(n-1):
        
        if road[i][j] - road[i+1][j] == 1: #내리막
            for k in range(i+1, i+l+1):
                if k >= n:
                    cantflag = 1
                    break
                if road[k][j] != road[i+1][j]:
                    cantflag = 1
                    break
                if visited[k][j] == 1:
                    cantflag =1
                    break
                visited[k][j] = 1
            if cantflag == 1:
                break
        elif road[i][j] - road[i+1][j] == -1: #오르막
            for k in range(i, i-l, -1):
                if k < 0:
                    cantflag = 1
                    break
                if road[k][j] != road[i][j]:
                    cantflag = 1
                    break
                if visited[k][j] == 1:
                    cantflag = 1
                    break
                visited[k][j] = 1
            if cantflag == 1:
                break
        elif road[i][j] == road[i+1][j]:
            pass
        else:
            cantflag = 1
            break
    
        
    if cantflag == 0:
        cnt += 1    
print(cnt)