import sys
from collections import deque
x, k = map(int, sys.stdin.readline().split())
q = deque()
q.append(x)
visited = [0]* (10**5+20)
def bfs():
    while q:
        n = q.popleft()
        if n == k:
            print(visited[n])
            break
        #bfs에선 연산의 순서도 매우매우매우매우...중요하다!!!
        if 2*n >= 0 and 2*n <= 100000:
            if visited[2*n] == 0:
                q.append(2*n)
                visited[2*n] = visited[n]
        if n-1 >= 0 and n-1 <= 100000:
            if visited[n-1] == 0:
                q.append(n-1)
                visited[n-1] = visited[n] + 1
        if n+1 >= 0 and n+1 <= 100000:
            if visited[n+1] == 0:
                q.append(n+1)
                if 2*n == n+1: #반례 : 1 2 출력 = 0 이어야하는데, 
                    #지금처럼 이렇게 예외 안잡아놓으면 2*n에서 잘 했다가 
                    #n+1때 visited[2]를 1로 만드는대참사발생함
                    visited[n+1] = visited[n]
                else:
                    visited[n+1] = visited[n] + 1
        
bfs()