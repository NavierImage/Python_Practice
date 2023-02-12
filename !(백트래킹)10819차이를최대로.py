import sys
n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [0] * n
haha = []
#순열 같은 경우 visited 배열로 해결가능.
def backtrack(nums, order):
    if len(nums) == order:
        cnt = 0
        for i in range(0, len(nums)-1):
            cnt += abs(nums[i] - nums[i+1])
        
        haha.append(cnt)
    else:
        for i in range(order):
            if visited[i] == 0:
                nums.append(num_list[i])
                visited[i] = 1
                backtrack(nums, order)
                nums.pop(-1)
                visited[i] = 0

backtrack([], n)
print(max(haha))