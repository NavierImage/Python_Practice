import sys
import re
from collections import deque
tc = int(sys.stdin.readline())
res = []
for _ in range(tc):
    f = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()
    deck = deque(re.findall(r'\d+', a))
    mode = 0; flag = 0
    for i in range(len(f)):
        if f[i] == 'R' and mode == 0:
            mode = 1 #mode0인상태에서 'R'입력 들어오면 mode 1로 바뀜
        elif f[i] == 'R' and mode == 1:
            mode = 0 #mode1인 상태에서 'R'입력 들어오면 mode 0으로 바뀜
        elif f[i] == 'D' and mode == 0:
            if len(deck) == 0: #오류처리는 이부분에서만 하면됨. 다른곳 건드리니 에러가..
                flag = 1
                break
            deck.popleft() #mode0이면 앞에서 제거
        elif f[i] == 'D' and mode == 1:
            if len(deck) == 0:
                flag = 1
                break
            deck.pop() #mode1이면 뒤에서 제거
    if flag:
        res.append('error')
        continue
    tmp1 = '['; tmp2 = ']'; num = []

    if mode == 0: #원하는 출력을 생성해주는 부분
        while deck:
            num.append(deck.popleft())
        tmp = ''
        if len(num) != 0:
            tmp = ','.join(num)
        tmp = tmp1+tmp+tmp2

    elif mode == 1:
        while deck:
            num.append(deck.pop())
        tmp = ''
        if len(num) != 0:
            tmp = ','.join(num)
        tmp = tmp1+tmp+tmp2

    
    res.append(tmp)

for i in res:
    print(i)