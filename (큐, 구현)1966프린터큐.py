import sys
from collections import deque
TC = int(sys.stdin.readline().rstrip())
result =[]
for _ in range(TC):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    pque = deque() #우선순위를 담을 큐
    oque = deque() #문서의 순서를 담을 큐
    prty = list(map(int, sys.stdin.readline().rstrip().split()))
    j = -1
    for i in prty: 
        j += 1 #문서의 순서
        pque.append(i) #우선순위
        oque.append(j) #문서의 순서 (튜플,리스트는 인덱싱이 힘듦)
    
    iter = 0
    while(1):
        p = pque.popleft()
        o = oque.popleft()
        if p == max(prty): #만약 최고 중요도면
            iter += 1 #프린터 출력횟수 1 증가
            prty[prty.index(max(prty))] = -1 #최고 중요도인거 뽑앗으므로 그것을 -1로 바꿔줌(없는것으로 만들기)
            #설사 최고중요도 같은게 여러개라도, 앞에서 부터 뽑을 것이기에 괜찮음
            if o == m:
                result.append(iter) #만약 중요도 p번째에 뽑을 문서가 m번째 문서일 경우 출력횟수인 iter를 result로
                break
        else: #최고 중요도가 아니라면 다시 큐에 넣어줌
            pque.append(p)
            oque.append(o)   

for i in result:
    print(i)
#acmicpc.net/problem/1966