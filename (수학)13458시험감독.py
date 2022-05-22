n = int(input())
mans=  list(map(int, input().split()))
b, c = map(int, input().split())
need= 0
for i in mans:
    i -= b #총감독자의 감시수는 무조건 빼고
    need += 1
    if i <= 0 :
        continue #있는 인원보다 감시를 많이 할수 있으면 그냥 다음꺼로
    
    if i % c != 0:
        need += i // c + 1 #나머지 0 넘으면 몫+1
    else:
        need += i // c #나머지 0이면 걍 몫임

print(need)
        