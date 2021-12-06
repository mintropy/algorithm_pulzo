"""
Title : 카드 섞기
Link : https://www.acmicpc.net/problem/1091
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def shuffle(cards_shuffle, cards_state):
    next_state = [0] * N
    for i in range(N):
        next_state[cards_shuffle[i]] = cards_state[i]
    return next_state


def check(cards_state, check_state):
    if cards_state == check_state:
        return True
    return False


N = int(input())

cards_state = list(MIIS())
cards_shuffle = list(MIIS())

initial_state = cards_state[::]
goal_state = [0, 1, 2] * (N // 3)
shuffle_count = 0

while True:
    if check(cards_state, goal_state):
        print(shuffle_count)
        break
    cards_state = shuffle(cards_shuffle, cards_state)[::]
    shuffle_count += 1
    if check(cards_state, initial_state):
        print(-1)
        break


'''
N = int(input())

cards_state = list(MIIS())
cards_shuffle = list(MIIS())

initial_state = cards_state[::]
goal_state = [0, 1, 2] * (N // 3)
shuffle_count = 0
while True:
    if cards_state == goal_state:
        print(shuffle_count)
        break
    # for i in range(N):
    #     if cards_state[i] != i % 3:
    #         break
    # else:
    #     print(shuffle_count)
    #     break
    next_state = [0] * N
    for i in range(N):
        next_state[cards_shuffle[i]] = cards_state[i]
    cards_state = next_state[::]
    shuffle_count += 1
    if cards_state == initial_state:
        print(-1)
        break
'''
