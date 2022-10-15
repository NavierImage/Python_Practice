import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

throw = int(sys.stdin.readline().rstrip())
throw_list = list(map(int, sys.stdin.readline().rstrip().split()))

def find_cluster(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    cluster = []
    cluster.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and arr[nx][ny] == 'x':
                    cluster.append((nx, ny))
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    #cluster.sort(key=lambda x: (x[0], x[1]))

    return cluster

for th in range(throw):
    visited = [[0] * m for i in range(n)]
    if th % 2 == 0:
        left_throw = 1
    else:
        left_throw = 0
    
    destroy_row = throw_list[th]
    if left_throw == 1:
        for col in range(m):
            if arr[n-destroy_row][col] == 'x':
                arr[n-destroy_row][col] = '.'
                break
    else:
        for col in range(m-1, -1, -1):
            if arr[n-destroy_row][col] == 'x':
                arr[n-destroy_row][col] = '.'
                break
    
    cluster_list = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'x' and visited[i][j] == 0:
                cluster = find_cluster(i, j)
                cluster_list.append(cluster)
    
    ###어떤 물체를 둘러싼 네모선 잡기(대각위점, 대각아래점)####
    ###최대 최소값을 업데이트 하는방식####
    for idx in range(len(cluster_list)):
        x1 = n; x2 = -1; y1 = m; y2 = -1

        for i in range(len(cluster_list[idx])): ###사각포인트 잡기###
            a, b = cluster_list[idx][i] 
            if x1 > a:
                x1 = a
            if x2 < a:
                x2 = a
            if y1 > b:
                y1 = b
            if y2 < b:
                y2 = b
    ############################################################

    ##네모박스중 아래에 존재하는 'x'찾는부분##
        below_point_list = []
        for j in range(y1, y2+1):
            for i in range(x2, x1-1, -1):
                if arr[i][j] == 'x':
                    if (i, j) in cluster_list[idx]:
                        below_point_list.append((i, j))
                    
                        break
        
    ## 아래에 존재하는 x중 밑의 다른 클러스터 or 땅까지의 거리중 가장 가까운 거리 검색 ##
        temp_dist_list = []
        for j in range(y2+1-y1):
            a, b = below_point_list[j]
            if a == n-1:
                temp_dist_list.append(0)
                continue
            for i in range(a+1, n):
                if arr[i][b] == 'x' and (i, b) not in cluster_list[idx]:
                    temp_dist_list.append(i - a - 1)
                    break
                elif arr[i][b] == '.' and i == n-1:
                    temp_dist_list.append(n - a - 1)
        descent = min(temp_dist_list) 
        
    #### descent만큼 떨어진다###
    ### 먼저 없앨 거 '.'로 바꾸고###
    ### 그 다음 'x'로 업뎃해준다###
        for i in range(len(cluster_list[idx])):
            a, b = cluster_list[idx][i]
            arr[a][b] = '.'
        for i in range(len(cluster_list[idx])):
            a, b = cluster_list[idx][i]
            arr[a+descent][b] = 'x'
    
for i in arr:
    for j in i:
        print(j, end='')
    print()
