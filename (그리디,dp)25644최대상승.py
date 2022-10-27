import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

min_ = 10**9+1
max_ = arr[-1]
sell = 0
nominate = []
for i in range(len(arr)-1, -1, -1):
    if min_ > arr[i]:
        min_ = arr[i]
    if max_ - min_ > sell:
        sell = max_-min_
    if max_ < arr[i]: #기존 최댓값보다 더 큰값이 나오면, 그 상태에서 결과 저장
        max_ = arr[i]
        min_ = arr[i]
        nominate.append(sell)
nominate.append(sell)
#저장된 결과들에서 최댓값 뽑아내기
print(max(nominate))