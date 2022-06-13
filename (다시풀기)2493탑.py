import sys
n = int(sys.stdin.readline().rstrip())
top = list(map(int, sys.stdin.readline().rstrip().split()))
td = [0]
stack = []
for i in range(len(top)-1):
    stack.append([i, top[i]])
    while stack:
        if stack[-1][1] < top[i+1]: #기준 top보다 작다면 스택에잇는거 pop시켜보고 다시
            stack.pop()
            
        else:
            td.append(stack[-1][0]+1) #stack안에 있는 인덱스를 추가, 때문에 첫번째거 0으로 시작해야함.(언제나 n-1의 결과)
            break
    if len(stack) == 0:
        td.append(0)           

print(*td)