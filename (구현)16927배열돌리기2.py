import sys
from collections import deque
n, m, r = map(int, sys.stdin.readline().rstrip().split())
p = min(n, m)

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

###고리는 직선으로 나타낼수 있다는것..###
ro_list = []
for t in range(p//2):
    queue = deque()
    for i in range(t, n-t):
        queue.append(arr[i][t])
    for j in range(t+1, m-t):
        queue.append(arr[n-1-t][j])
    for i in range(n-2-t, t-1, -1):
        queue.append(arr[i][m-1-t])
    for j in range(m-2-t, t, -1):
        queue.append(arr[t][j])
    ro_list.append(queue)

##돌리기 함수##
def rotate(idx):
    queue = ro_list[idx]
    queue.appendleft(queue.pop())
    ro_list[idx] = queue
    
nums = []
for i in range(p//2):
    a = 2 * (n-2*i + m-2*i) - 4
    nums.append(r % a)

for idx in range(len(ro_list)):
    for i in range(nums[idx]):
        rotate(idx)

##돌린것 다시 배치하는 부분##
##수학적 관계로 하면시간 줄일듯##
return_arr = [[0] * m for _ in range(n)]
idx = 0
for t in range(p//2):
    cnt = 0
    for i in range(t, n-t):
        return_arr[i][t] = ro_list[idx][cnt]
        cnt += 1
    for j in range(t+1, m-t):
        return_arr[n-1-t][j] = ro_list[idx][cnt]
        cnt += 1
    for i in range(n-2-t, t-1, -1):
        return_arr[i][m-1-t] = ro_list[idx][cnt]
        cnt += 1
    for j in range(m-2-t, t, -1):
        return_arr[t][j] = ro_list[idx][cnt]
        cnt += 1
    idx += 1

for i in return_arr:
    print(*i)