'''
숫자 할리갈리 게임

'''
import sys

N, M = map(int,sys.stdin.readline().split())
from collections import deque

do_cards = deque()
su_cards = deque()
for _ in range(N):
    A, B = map(int,sys.stdin.readline().split())
    do_cards.append(A)
    su_cards.append(B)

do_ground = deque()
su_ground = deque()

while M > 0:
    # 도 부터 시작
    A = do_cards.pop()
    do_ground.append(A)
    # 횟수 줄이기
    M -= 1
    # do의 카드 덱이 비면
    if len(do_cards) == 0:
        break
    # 도가 이기는 경우
    if A == 5:
        do_cards.extendleft(su_ground)
        do_cards.extendleft(do_ground)
        do_ground = deque()
        su_ground = deque()
    # 수가 이기는 경우
    if do_ground and su_ground:
        if do_ground[-1] + su_ground[-1] == 5:
            su_cards.extendleft(do_ground)
            su_cards.extendleft(su_ground)
            do_ground = deque()
            su_ground = deque()
    # 횟수가 끝날 때.
    if M == 0:
        break
    
    # 수 확인.
    B = su_cards.pop()
    su_ground.append(B)
    M -= 1
    if len(su_cards) == 0:
        break
    if B == 5:
        do_cards.extendleft(su_ground)
        do_cards.extendleft(do_ground)
        do_ground = deque()
        su_ground = deque()
    if do_ground and su_ground:
        if do_ground[-1] + su_ground[-1] == 5:
            su_cards.extendleft(do_ground)
            su_cards.extendleft(su_ground)
            do_ground = deque()
            su_ground = deque()

if len(do_cards) > len(su_cards):
    print('do')
elif len(do_cards) < len(su_cards):
    print('su')
else:
    print('dosu')