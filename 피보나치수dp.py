import sys
sys.setrecursionlimit(10**8)
n = sys.stdin.readline().rstrip()
n = eval(n)
dp = [0]*(10**5)
def fibonacci(n):
    global dp
    if n == 0: 
        dp[n] = n
        return 0
    if n == 1:
        dp[n] = n
        return 1
    else: 
        if dp[n-1] == 0:
            dp[n-1] = fibonacci(n-1) 
            b = dp[n-1]
        else:
            b = dp[n-1]

        if dp[n-2] == 0:
            dp[n-2] = fibonacci(n-2)
            a = dp[n-2]
        else:
            a = dp[n-2]
        return a + b
    
print(fibonacci(n))
