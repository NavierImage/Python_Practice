import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

dp = [[10**8] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j // coin[i-1] >= 1: #j원을 i-1번째 동전으로 나누고 몫이 1이상인경우(~~j원이 현재 coin보다 큰경우)(i=1:n까지)
            #먼저 최소로 가능한거 봐주고... ex) 반례 (2, 10) 2 3 정답은 4(2 두개 3 두개)
            #7까지 만드는 경우의 수를 저장해줘야함. 
            dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coin[i-1]]) 
            
            if j % coin[i-1] == 0: #나누어 떨어질 경우
                dp[i][j] = min(dp[i][j], j//coin[i-1])
            else: #나누어 떨어지지 않을 경우
                dp[i][j] = min(dp[i][j], j//coin[i-1] + dp[i-1][j-coin[i-1]*(j//coin[i-1])]) # ex) 1원 9개 로 9를만드는 상황에서 1원 4개 5원 1개로 바꿀때 (나머지 제거한 몫)* (원래 수)

        else: # 조건 만족하지 않으면 기존꺼 (n-1 행)
            dp[i][j] = dp[i-1][j]

# print(dp)
# for d in dp:
    # print(d)
if dp[n][k] == 10**8:
    print(-1)
else:
    print(dp[n][k])