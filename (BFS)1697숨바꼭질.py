from collections import deque
n, k = map(int, input().split())

q = deque()
q.append((n, -1)) #cnt정보와함께 queue에 담기!
visited=[0]*(10**5)*2 #넉넉하게 잡기
#visited에 넣어놓으면 다 탐색해야해서
#지수적으로늘려가는 BFS특성상 시간도 지수로 늘게됨
#먼저 공간잡아놓고 방문처리를 하는식으로해야!
while q:
    x, cnt = q.popleft() #이렇게해야 반복때마다 cnt가 안 오르고 경로마다 횟수 저장가능!
    cnt+=1
    if x == k :
        break
    if 2*x<= 100000 and 2*x >= 0:#인덱스 오류때문에 이렇게 먼저 잡아줘야(리스트 밖으로 튕기면안되니..)
        if visited[2*x] == 0:
            q.append((2*x, cnt))
            visited[2*x] =1
    if x+1<= 100000 and x+1>=0:
        if visited[x+1] == 0 :
            q.append(((x+1), cnt))
            visited[x+1] =1 

    if x-1>=0 and x-1 <= 100000:
        if visited[x-1] == 0:
            q.append(((x-1), cnt))
            visited[x-1] =1

print(cnt)
#https://www.acmicpc.net/problem/1697