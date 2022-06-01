n, m = map(int, input().split())
num = list(map(int, input().split()))
s = []
num.sort()
def dfs(s):
    if len(s) == m:
        print(*s)
        return
    else:
        for i in num:
            if len(s) >= 1:
                if i < s[len(s)-1]:
                    continue

            s.append(i)
            dfs(s)
            s.pop()

dfs(s)

