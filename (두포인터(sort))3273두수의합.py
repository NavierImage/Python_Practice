n = int(input())
num = list(map(int, input().split()))
m = int(input())
x = 0
y = n - 1
num.sort()
cnt = 0
#두개의 포인터 조정해가며 푸는 문제
#두수의 합이지만 부분합을 계산할 때도 쓸수있는 알고리즘일듯
while(1):
    if x >= y:
        break

    if num[x] + num[y] < m:
        x += 1
    elif num[x] + num[y] > m:
        y -= 1
    else:
        x += 1
        y -= 1
        cnt += 1

print(cnt)
#https://www.acmicpc.net/problem/3273