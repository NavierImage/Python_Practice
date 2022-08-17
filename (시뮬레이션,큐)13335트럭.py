import sys
from collections import deque
n, w, L = map(int, sys.stdin.readline().rstrip().split())
queue = deque(map(int, sys.stdin.readline().rstrip().split()))
bridge = [0] * w

cnt = 0
while True:
    if len(queue) != 0:
        if sum(bridge) + queue[0] <= L:
            bridge.pop(0)
            cnt += 1
            bridge.append(queue.popleft())
        else:
            if sum(bridge) - bridge[0] + queue[0] <= L:
                bridge.pop(0)
                cnt += 1
                bridge.append(queue.popleft())
            else:
                bridge.pop(0)
                bridge.append(0)
                cnt += 1
    else:
        if sum(bridge) > 0:
            bridge.pop(0)
            bridge.append(0)
            cnt += 1
        else:
            break
print(cnt)
