import sys
n = int(sys.stdin.readline().rstrip())
givonn = []
for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    givonn.append(t)
nums = list(set(givonn))

nums.sort()

for i in nums:
    print(i)
#https://www.acmicpc.net/problem/10989
#직접 정렬알고리즘만들어서 다시풀어보기

