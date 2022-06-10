import sys
##########소수판별 알고리즘###########
# 루프 1 : 판별 대상부터 상한까지 
# 루프 2 : 2부터 정수화한 루트i 까지 ( +1해줘야 )
# i가 j로 나눠진다면 나가고
# 하나도 안 나눠졌다면 이걸 소수로 판정
prime = []
for i in range(2, 1100):
    for j in range(2, int(i**(0.5)) + 1):
        if i % j == 0:
            break
    else:
        prime.append(i)

n = int(sys.stdin.readline().rstrip())
numlist = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for i in numlist:
    if i in prime:
        cnt += 1

print(cnt)
#https://www.acmicpc.net/problem/1978