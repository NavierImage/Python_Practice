import sys
from collections import deque
n = int(sys.stdin.readline())
seq = deque()
for _ in range(n):
    t = int(sys.stdin.readline())
    seq.append(t)

stack = deque()
i = 0
rst = []
#문제이해가 좀어려웠음
#지울때 빼고는 i가 증가하여 스택에 push되고,
#지울땐 i변하지 않고 pop됨.
#반례 조건 찾기가 까다로웠음..
while seq:
    if len(stack) == 0 and len(seq) != 0: #반례1
        if seq[0] <= i:
            print('NO')
            quit()
    if len(stack) == 0:
        i+= 1
        stack.append(i) 
        rst.append('+')

    elif len(stack) != 0:
        if stack[len(stack) -1] < seq[0]:
            if i > seq[0]: #이런걸 발견하기 너무 어렵다....반례2
                print('NO')
                quit()
            i += 1
            stack.append(i)
            rst.append('+')
        elif stack[len(stack) -1] > seq[0]:
            stack.pop()
            rst.append('-')
        else:
            seq.popleft()
            stack.pop()
            rst.append('-')
    
for i in rst:
    print(i)
#https://www.acmicpc.net/problem/1874