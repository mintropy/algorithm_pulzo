import sys
from heapq import *
input = sys.stdin.readline
N = int(input())
# 시작 종료 시간
inout = [list(map(int, input().split())) for _ in range(N)]
inout.sort()
# 다음 사용자가 사용할 컴퓨터 힙
seat = []
# 나가는 이용자 힙
out = []
# 컴퓨터별 이용횟수
cnt = []
# 필요 컴퓨터 수
idx = 0

for s, e in inout:
    while out:
        if out[0][0] < s:
            heappush(seat, heappop(out)[1])
        else: break
    if seat:
        this = heappop(seat)
        heappush(out, [e, this])
        cnt[this] += 1
    else:
        cnt.append(1)
        heappush(out, [e, idx])
        idx += 1
print(idx)
print(*cnt)