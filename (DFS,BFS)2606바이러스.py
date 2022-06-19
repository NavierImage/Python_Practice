import sys
node_num = int(sys.stdin.readline().rstrip())
edge = int(sys.stdin.readline().rstrip())

graph = {}
for _ in range(edge):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    try:graph[start].append(end)
    except:graph[start] = [end]
    try:graph[end].append(start)
    except:graph[end] = [start]

visited = []
def dfs(node):
    if node in graph and node not in visited: #key가 graph에 있고, 만약 방문하지 않았다면.
        visited.append(node)
        for i in range(len(graph[node])): #옆으로 꺾는부분
            dfs(graph[node][i]) #깊게 들어가는 부분(이게 우선적으로 진행된다)
dfs(1)
if len(visited) == 0:
    print(0)
else:print(len(visited)-1)