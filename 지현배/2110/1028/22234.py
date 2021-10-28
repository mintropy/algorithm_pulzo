import sys
from collections import deque
input = sys.stdin.readline
N, T, W = map(int, input().split())
queue = deque([list(map(int, input().split())) for _ in range(N)])
M = int(input())
next = deque(sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[2]))
current_time = 0
ans = ''
while queue and current_time < W:
    px, tx = queue.popleft()
    # tx 가 T 보다 작거나 같을 때
    if tx <= T:
        if current_time + tx < W:
            ans += (str(px) + '\n') * tx
        # 현재 시간 + 업무 처리 시간이 W 이상일 때
        else:
            ans += (str(px) + '\n') * (W - current_time)
        current_time += tx
    # tx 가 T 보다 클 때
    else:
        if current_time + T < W:
            ans += (str(px) + '\n') * T
        # 현재 시간 + 업무 처리 시간이 W 이상일 때
        else:
            ans += (str(px) + '\n') * (W - current_time)
        current_time += T
    # 업무 처리 동안 들어온 손님을 큐에 추가
    while next and next[0][2] <= current_time:
        npx, ntx, _ = next.popleft()
        queue.append([npx, ntx])
    # 업무가 안 끝난 손님은 맨 뒤로
    if tx > T:
        queue.append([px, tx - T])
print(ans.rstrip())