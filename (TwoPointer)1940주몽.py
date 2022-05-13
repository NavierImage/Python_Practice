#투포인터(브루트 포스로도 풀수는 있으나 느리다)
n = int(input())
m = int(input())
num = list(map(int, input().split()))
num.sort() 
#투포인터를 사용하기위해선 정렬을 먼저해야함
#그래야 올리고 내리고 할때 규칙이 맞으니깐

x = 0
y = n - 1
dama = 0

while(1):
    if x >= y: #만약 작은포인터가 큰포인터보다 커지면 전부 확인한 것이므로 바로 루프탈출
        break
    if num[x] + num[y] < m: #목표수보다 작으면 작은 포인터를 올려주고
        x += 1
    elif num[x] + num[y] > m: #목표수보다 크면 큰 포인터를 내려준다
        y -= 1
    else:
        dama += 1 #목표수에 도달하면 다마에 담아준다
        x += 1 #전부 세야하니 작은포인터 올려주고 큰포인터 내려주기
        y -= 1    
print(dama)       
#https://www.acmicpc.net/problem/1940