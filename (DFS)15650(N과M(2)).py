n, m = map(int, input().split())
num = []

def dfs(num, n, m, visited= [0]*(n)): #방문 체크 리스트 하나 설치
    if len(num) == m:
        print(*num)
    else:
        for i in range(1, n+1):
            if visited[i-1] == 1: #방문 했다면 넘기기
                continue
            num.append(i)
            visited[i-1] = 1 #먼저 추가하고 방문 체크리스트를 1로 
            dfs(num, n, m, visited) #여태까지 체크리스트들고 들어가기
            num.pop()
            for j in range(i, n): #처음 인덱스만 빼고, 방문체크리스트 0으로 초기화해줌
                visited[j] = 0
dfs(num, n, m)