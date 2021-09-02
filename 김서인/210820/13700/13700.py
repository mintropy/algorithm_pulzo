import sys
from collections import deque

input = sys.stdin.readline

N, S, D, F, B, K = map(int, input().split())
chk = [0] * (N + 100000)  # 방문했던 곳에 다시 방문하면 최소가 아니다 -> 방문 체크해서 방문한 곳 다시 안 가게 함.

if K != 0:
    police_offices = list(map(int, input().split()))

    # 경찰서는 방문하면 안되니, 방문 체크
    for police_office in police_offices:
        chk[police_office] = 1

button_cnts = []

q = deque()
q.append((S + F, 1))  # 현재 도둑의 위치, 몇번 좌우 버튼을 눌렀는지
q.append((S - B, 1))
while q:
    idx, cnt = q.popleft()
    if 0 < idx <= N and 0 < cnt <= N:  # 마포구를 벗어나지 않아야 하고
        if idx == D:  # 도둑이 집에 잘 도착
            button_cnts.append(cnt)

        if chk[idx + F] == 0:  # 앞으로
            chk[idx + F] = 1
            q.append((idx + F, cnt + 1))

        if chk[idx - B] == 0:  # 뒤로
            chk[idx - B] = 1
            q.append((idx - B, cnt + 1))

if button_cnts:
    print(min(button_cnts))
else:
    print('BUG FOUND')
