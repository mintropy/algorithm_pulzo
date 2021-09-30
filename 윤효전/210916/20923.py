from collections import deque
from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
do = deque()
su = deque()
for _ in range(N):
    a, b = map(int, input().split())
    do.append(a)
    su.append(b)

do_g = []
su_g = []

for i in range(M):
    if i % 2 == 0:
        do_g.append(do.pop())
    else:
        su_g.append(su.pop())

    if not do or not su:
        break

    # 도도가 가져 간다
    if (do_g and do_g[-1] == 5) or (su_g and su_g[-1] == 5):
        for n in su_g:
            do.appendleft(n)
        su_g.clear()
        for n in do_g:
            do.appendleft(n)
        do_g.clear()

    # 수연이 가져 간다
    if do_g and su_g and do_g[-1] + su_g[-1] == 5:
        for n in do_g:
            su.appendleft(n)
        do_g.clear()
        for n in su_g:
            su.appendleft(n)
        su_g.clear()

if len(do) > len(su):
    print('do')
elif len(do) < len(su):
    print('su')
else:
    print('dosu')
