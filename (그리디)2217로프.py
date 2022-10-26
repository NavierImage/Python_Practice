import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort(reverse=True)
max_ = 0
min_ = 10001
s = 0
for i in range(n):
    s += arr[i]
    if arr[i] < min_:
        min_ = arr[i]
    if max_ < min_ * (i+1):
        max_ = min_ * (i+1)
    
print(max_)