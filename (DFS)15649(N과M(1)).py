n, m = map(int, input().split())
num = []
def dfs(num, n, m): #빈 리스트 먼저 선언
    if len(num) == m:
        print(*num) #만약 출력하고싶은 길이와 같은 곳에 도달하면 print함
        
    else:
        for i in range(1, n + 1): #i를 리스트에 넣어주기
            if i in num: #i가 이미 있다면 다시 반복
                continue
            num.append(i) #num에 i 추가 
            dfs(num, n, m) #추가하고 스택쌓음(그니깐 num의 개수가 m이 되지않으면, 계속 들어감)
            num.pop() #m이되면 pop함 이게 쌓인 함수 스택마다 다 pop되어서 결국 num리스트는 0이됨
        
dfs(num,n,m)       