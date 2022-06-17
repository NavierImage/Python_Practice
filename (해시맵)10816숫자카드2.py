import sys
n = int(sys.stdin.readline().rstrip())
numset = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
findthis = list(map(int, sys.stdin.readline().rstrip().split()))
fnumdict = {}
for i in findthis:
    fnumdict[i] = 0 #찾아야할것들 딕셔너리화
for i in numset:
    try: fnumdict[i] += 1 #numset돌면서 잇으면 딕셔너리에 있는거 +=1
    except: pass

for i in findthis: #좀 이상하고 더러운 반례때매 이렇게짬ㅋㅋ
    try:print(fnumdict[i], end = ' ')
    except:pass
#딕셔너리 진짜 powerful한듯
#https://www.acmicpc.net/problem/10816