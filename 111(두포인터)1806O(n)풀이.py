import sys
n, s = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))
#애초에 합을 하고 가져가는식으로 바꿔야함 논리자체는 지금 정확
x = 0
y = 1
parsum = seq[0]
res = []

while(1):
    if parsum>= s: #크거나 같으면 무조건 res에 추가
        res.append(y - x)

    if y == len(seq): #만약 y가 수열의 끝 인덱스와 같다면 x만건드리기
        parsum -= seq[x]
        x += 1
    else: #y가 수열의 끝 인덱스와 같지않다면 x와 y둘다 조절
        if parsum >= s: #부분합이 기준값보다 크면
            parsum -= seq[x] #수열에서 x+1번째 값을 빼고
            x += 1 #x인덱스 앞으로 옮기기
            if y - x == 1: #만약 부분합 수열의 원소가 한개라면
                parsum += seq[y] #y인덱스도 앞으로 옮겨줘야함
                y += 1
        elif parsum < s: #부분합이 기준값보다 작다면
            if y != len(seq): #이부분은 없어도될거같은데.. 
                parsum += seq[y] #수열에서 y+1번째 값을 합쳐주고
                y += 1 #y인덱스 더해주기

    if x == len(seq): #x도 끝인덱스에 도달했다면 종료
        break
if len(res) == 0:
    print(0)
else: print(min(res))
#https://www.acmicpc.net/problem/1806
