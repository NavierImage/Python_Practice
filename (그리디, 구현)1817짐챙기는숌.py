import sys
n, m = map(int, input().split())
if n == 0:
    print(0)
    sys.exit() #0일시 종료
book = list(map(int, input().split())) #순서대로 리스트에 저장
cnt = 0
i = 0
sack = 0
while(1):
    
    if len(book) == 0:
        cnt += 1
        break 

    bpre = book[:] #가방이 넘칠 경우를 위해 이전 상태를 저장해둠, 깊은복사
    #만약 리스트의 첫 번째 값이 제한 값보다 작으면 없애고 가방에 넣어줌
    if book[i] <= m:
        sack += book[i]
        book.remove(book[i]) 
    
    if sack > m: #가방이 넘쳤을 경우 없애기 전의 리스트로 돌려놓음
        book = bpre 
        sack = 0
        cnt += 1 #가방을 하나 쓴거이므로 count해줌
    elif sack == m: #가방 제한에 딱 맞을 경우엔 굳이 돌려놓을 필요는 없고 count만 해줌
        sack = 0
        cnt += 1
        if len(book) == 0: #만약 딱 맞는 경우고, 남은게 없을 경우 바로 나가줌 (위에서 중복으로 count하지않게)
            break
    
print(cnt)
#https://www.acmicpc.net/problem/1817