import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = {}
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split()) #딕셔너리를 이용한 그래프 구현법...
    if start in graph: #시작지점이 그래프에 있으면
        if end not in graph[start]: #끝지점의 시작(key)값의 value에 없으면
            graph[start].append(end) #value는 리스트값이므로 거기에 append
    elif start not in graph: #만약 start 값이 없다면
        graph[start] = [end] #딕셔너리[키] = value ( 지금은 value가 리스트 ) #end값 가진 list로 추가해줌

    if end in graph: #end key값이 있다면
        if start not in graph[end]: #value list에 추가해줌
            graph[end].append(start)
    elif end not in graph: #end값이 없다면
        graph[end] = [start]

#딕셔너리를 정렬할수 있도록.... 
#이런구현 시간 박살남 다시풀기
q = deque()
rst = []
q.append([1, 0])
visited = [0] * (n + 1)
def bfs():
    while q:
        key, cnt = q.popleft()
        cnt += 1
        for i in graph.keys():
            if i == key:
                visited[i] = 1
                for j in graph[i]: #3중반복이 들어가므로 시간면에서 그냥 메롱됨 ㅋㅋㅋ ;;
                    if visited[j] == 1:
                        continue
                    visited[j] = 1
                    q.append((j, cnt))
                    rst.append([j, cnt])
            
bfs()
m = 0
for i in rst:
   if m < i[1]:
       m = i[1]
odr = 10**5
scnt = 0
for i in rst:
    if i[1] == m:
        scnt += 1
        if odr > i[0]:
            odr = i[0]
print(odr, m, scnt)
#https://www.acmicpc.net/problem/6118