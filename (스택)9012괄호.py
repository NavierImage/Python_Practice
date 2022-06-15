import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
string = []
for _ in range(n):
    string.append(sys.stdin.readline().rstrip())

result = []
#스택을 구현 안하고 카운터로 판단해도 된다.
#예전에 계산기 구현에서 스택을 몰라 재귀로 구현해봤던 생각이 남.
for ps in string:
    stk = deque()
    noflag = 0
    for j in range(len(ps)):
        if ps[j] == '(':
            stk.append('(')
        elif ps[j] == ')': 
            if len(stk) > 0: 
                stk.pop()
            else: #만약 '('의 개수보다 ')'의 개수가 더많다면
                result.append('NO')
                noflag = 1
                break
    if len(stk) == 0 and noflag == 0: #스택에 남아있는 것도 없고 noflag에 걸리지않은거.
        result.append('YES') 
    elif len(stk) > 0 : #만약 '('의 개수가 ')'보다 더 많다면 스택에 남아있을 것이므로
        result.append('NO')
for i in result:
    print(i)