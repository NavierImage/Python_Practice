import sys 
sys.setrecursionlimit(10**8)

def dfs(num_str, n):
    if len(num_str) == n:
        total_number_list.append(int(num_str))
        return
    else:
        for i in range(9, -1, -1):
            if len(num_str) <= 0:
                num_str = num_str + str(i)
                dfs(num_str, n)
                num_str = num_str[:-1]
            else:
                if i < int(num_str[-1]):
                    num_str = num_str + str(i)
                    dfs(num_str, n)
                    num_str = num_str[:-1]
total_number_list = []
for i in range(11):
    dfs("", i+1)
total_number_list.sort()

idx = int(sys.stdin.readline().rstrip())
try:
    print(total_number_list[idx-1])
except:
    print(-1)