import sys 
import copy
from itertools import permutations
n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

perm = []
for _ in range(k):
    row, col, su = map(int, sys.stdin.readline().rstrip().split())
    perm.append([row, col, su])
'''
pcr = []
p = []

def dfs(p):
    global pcr
    if len(p)==len(perm):
        pcopy = copy.deepcopy(p)
        pcr.append(pcopy)
        return
    else:
        for i in perm:
            if i in p:
                continue
            p.append(i)
            dfs(p)
            p.pop()
dfs(p)
'''
result =[]
#반례: 이반복문 자체가 작동하지 않는경우: pcr이 아예 비어있는경우.
#내가짠건 무엇이 문제인지?
for iter in permutations(perm, len(perm)):
    crr = copy.deepcopy(arr)
    for ord in iter:
        r, c, s = ord
        cnt = -1
        for __ in range((2*s+1)//2):
            cnt += 1

            for j in range(c-1-s+cnt, c+s-cnt):
                if j == c-1-s+cnt:
                    tmp = crr[r-1-s+cnt][j]
                    crr[r-1-s+cnt][j] = crr[r-s+cnt][j]
                else:
                    crr[r-1-s+cnt][j] ,tmp = tmp, crr[r-1-s+cnt][j]
            for i in range(r-1-s+cnt+1, r+s-cnt):
                crr[i][c+s-1-cnt], tmp = tmp, crr[i][c+s-1-cnt]
            for j in range(c+s-1-cnt-1, c-s-2+cnt, -1):
                crr[r+s-1-cnt][j], tmp = tmp, crr[r+s-1-cnt][j]
            for i in range(r+s-cnt-1-1, r-s+cnt-2, -1):
                crr[i][c-s-1+cnt], tmp = tmp, crr[i][c-s-1+cnt]
    armin = 10**7
    for i in crr:
        if sum(i) < armin:
            armin = sum(i)
    result.append(armin)

#반례: result없는경우...
print(min(result)) 
#https://www.acmicpc.net/problem/17406            