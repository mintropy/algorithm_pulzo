"""
Title : 가희와 은행
Link : https://www.acmicpc.net/problem/22234
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, T, W = MIIS()
# 처음 대기중 손님
guests = deque([tuple(MIIS()) for _ in range(N)])
M = int(input())
# 추가 들어올 손님
next_guests = sorted([tuple(MIIS()) for _ in range(M)], key=lambda x: -x[2])

# 지금 시간
time = 0
# 출력
output = []
while time < W:
    # 가장 앞에 있는 손님
    idx, left_time = guests.popleft()
    # 남아 있는 시간 비교
    # 더 많이 남아 있다면 T만큼만 하고 뒤로
    if left_time > T:
        # 시간 확인하여 출력
        next_time = time + T
        if next_time >= W:
            output += [idx] * (W - time)
        else:
            output += [idx] * T
        time = next_time
        # 다음 줄설수 잇는 손님 확인
        while next_guests:
            # 남은 손님이 있고, 출입 시간이 되었을 때
            if next_guests[-1][2] <= next_time:
                guests.append(next_guests[-1][:2])
                next_guests.pop()
            else:
                break
        # 줄 가장 뒤로
        guests.append((idx, left_time - T))
    # T와 같거나 적게 남아 있으면 퇴장
    else:
        # 시간 확인하여 출력
        next_time = time + left_time
        if next_time >= W:
            output += [idx] * (W - time)
        else:
            output += [idx] * left_time
        time = next_time
        # 다음 줄설수 잇는 손님 확인
        while next_guests:
            # 남은 손님이 있고, 출입 시간이 되었을 때
            if next_guests[-1][2] <= next_time:
                guests.append(next_guests[-1][:2])
                next_guests.pop()
            else:
                break
        # 은행 나가기

print(*output, sep='\n')
