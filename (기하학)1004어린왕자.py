T = int(input()) #고1 수학, 부등식의 영역 문제로 풀릴듯
star = []
for i in range(T):
    a = list(map(int, input().split())) #a = [시작x, 시작y, 끝점x, 끝점y]

    cnt = 0
    n = int(input()) #지날 행성계 몇개인지
    for j in range(n):
        b = list(map(int, input().split())) #b = [행성계x, 행성계y, 반지름]
        start = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2  #부등식의 영역, 시작점과 행성계 중심의 거리계산
        last = (a[2] - b[0]) ** 2 + (a[3] - b[1]) ** 2 #끝점과 행성계 중심의 거리계산
        if start < (b[2] ** 2) and last < (b[2] ** 2): #둘 다 한 행성계 안에있을경우, 해당 행성계의 경계를 안지나도됨
            continue

        if start < (b[2] ** 2): #반지름보다 작으면... 행성계 안 쪽에 있다는 것이므로 무조건 한번은 경계를 지나야함.
            cnt += 1
        
        if last < (b[2] ** 2):
            cnt += 1
    star.append(cnt)

for i in star:
    print(i)
#https://www.acmicpc.net/problem/1004