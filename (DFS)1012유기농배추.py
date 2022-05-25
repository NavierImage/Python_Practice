#1012
import sys
sys.setrecursionlimit(100000)
T = int(input())

def dfs(y, x):#y,x만 함수의 내부변수로 지정해주면됨
    if y < 0 or y >= n or x < 0 or x >= m: #외부영역으로 가려고 할시 바로 컷
        return False
    
    if bd[y][x] == 1: #배추가 있는곳은
        bd[y][x] = 0 #다 0으로 뒤집음
        dfs(y-1, x) #상하좌우에 대해 판단하면되는데, 
        dfs(y+1, x) #연결된 지점만 보려는 것이므로 
        dfs(y, x-1) #dfs함수를 통해 모두 상하좌우 방문처리를 함
        dfs(y, x+1) #어차피 외부영역으로 갈시엔 컷을 하므로 이렇게 해도됨!!!
        return True #재귀스택의 밑값만 True면, 연결된 영역에 한하여 방문처리가 모두 완료됨
    else:
        return False#끊어진 곳을 만나면 아무처리 안하고 바로 False

result = []
for z in range(T):
    bd = []
    m, n, k = map(int, input().split())
    rlt = 0
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        bd.append(temp)
    
    for ipt in range(k):
        c, r = map(int, input().split())
        bd[r][c] = 1
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j): #True면 +=1
                rlt += 1 

    result.append(rlt)
       
for i in result:
    print(i)
#https://www.acmicpc.net/problem/1012
