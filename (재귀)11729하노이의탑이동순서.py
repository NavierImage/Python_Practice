import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().rstrip())
logdata = []

###2개를 옮기는 경우를 생각하여 확장함###
###1. 위에있는거 tmp로 옮기고###
###2. 아래에 있는거 to로 옮기고###
###3. tmp에 있던거 to로 옮기는###
###것을 재귀로###
def hanoi(n, fr=1, tmp=2, to=3):
    if n == 1:
        logdata.append([fr, to])
        return None
    else:
        hanoi(n-1, fr, to, tmp)
        logdata.append([fr, to])
        hanoi(n-1, tmp, fr, to)
        
hanoi(n)
print(len(logdata))
for i in logdata:
    print(*i)