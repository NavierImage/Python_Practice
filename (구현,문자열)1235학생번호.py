import sys
n = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(n):
    nums.append(sys.stdin.readline().rstrip())

for i in range(len(nums[0])):
    temp = set(list(nums))
    if len(temp) == len(nums):
        for j in range(n):
            nums[j] = nums[j][1:]
    else:
        
        break
print(len(nums[0]) + 1)

