import sys
n = int(sys.stdin.readline().rstrip())
dp = [0]*(10**6+1)
dp[1] = 0
### 작은 문제부터 해결 (2 -> 1 인 문제)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 ## 2-> 1로 가는 방법은 1->1로 가는 방법의 +1 이다 (일단 빼기 1은 모두 가능하므로)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) ##  2로 나눠지는 경우, 앞서 구한 최소 방법의 수와 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) ## 3으로 나눠지는 경우, 앞서 구했던 최소 방법의 수와 비교함

print(dp[n])

