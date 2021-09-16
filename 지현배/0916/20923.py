import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
doca = deque()
suca = deque()
dogr = deque()
sugr = deque()
for _ in range(N):
    a, b = map(int, input().split())
    doca.append(a)
    suca.append(b)

for i in range(M):
    if i % 2 == 0:
        dogr.append(doca.pop())
        if len(doca) == 0:
            print('su')
            break
        # 도도 승리
        if dogr[-1] == 5:
            while sugr:
                doca.appendleft(sugr.popleft())
            while dogr:
                doca.appendleft(dogr.popleft())
        # 수연 승리
        if dogr and sugr and dogr[-1] + sugr[-1] == 5:
            while dogr:
                suca.appendleft(dogr.popleft())
            while sugr:
                suca.appendleft(sugr.popleft())
    else:
        sugr.append(suca.pop())
        if len(suca) == 0:
            print('do')
            break
        # 도도 승리
        if sugr[-1] == 5:
            while sugr:
                doca.appendleft(sugr.popleft())
            while dogr:
                doca.appendleft(dogr.popleft())
        # 수연 승리
        if dogr and sugr and dogr[-1] + sugr[-1] == 5:
            while dogr:
                suca.appendleft(dogr.popleft())
            while sugr:
                suca.appendleft(sugr.popleft())
else:
    if len(doca) > len(suca):
        print('do')
    elif len(doca) < len(suca):
        print('su')
    else:
        print('dosu')