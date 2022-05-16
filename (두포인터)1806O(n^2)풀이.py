import sys
n, s = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
#애초에 합을 하고 가져가는식으로 바꿔야함 논리자체는 지금 정확
x = 0
y = 1
parsum = 0
res = []
while(1):
    parsum = 0
    temp = []
    for i in range(x, y):
        parsum += seq[i]
        temp.append(seq[i])

    if parsum>= s:
        res.append(len(temp))

    if y == len(seq):
        x += 1
    else:
        if parsum >= s:
            x += 1
            if len(temp) == 1:
                y += 1
        elif parsum < s:
            if y != len(seq):
                y += 1

    if x == len(seq):
        break
if len(res) == 0:
    print(0)
else: print(min(res))
#https://www.acmicpc.net/problem/1806