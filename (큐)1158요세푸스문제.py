##1158
n, k = map(int, input().split())
lis = [i+1 for i in range(n)]
jos = []
i = -1 
cnt = 0 #인덱스 두개를 활용
while(1):
    i += 1
    cnt += 1 
    if len(lis) <= i: #lis를 줄이다가 i가 더 커지게 되면 처음인덱스로돌려줌
        i = 0

    if cnt == k: #cnt가 설정한 숫자가 되면 그때 lis[i]를 요세푸스 순열에 추가
        jos.append(lis[i])
        lis.pop(i)
        lis = lis[i:] + lis[:i]
        i = -1
        cnt = 0 #i값과 cnt값 초기화

    if len(lis) == 0: #비울 lis가 없으면 빠져나가기
        break

print('<',end='')
print(*jos,sep=', ',end='')
print('>')
#https://www.acmicpc.net/problem/1158    
    