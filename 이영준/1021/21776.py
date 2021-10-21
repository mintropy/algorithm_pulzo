"""
Title : 가희와 읽기 쓰기 놀이
Link : https://www.acmicpc.net/problem/21776
"""

import sys
input = sys.stdin.readline


def dfs(word_now: str):
    global n, cards, possible_output, turn, turn_now
    last_turn = True
    # 각 사람이 다른 카드를 더 낼 수 있는지 확인
    for i in range(n):
        x = turn_now[i]
        # 해당 사람 모든 행동 다 했을 때
        if x >= len(turn[i]):
            continue
        last_turn = False
        card_set = cards[turn[i][x]]
        word_next = calc_card(word_now, card_set)
        if word_next == 'ERROR':
            possible_output.add(word_next)
            continue
        turn_now[i] += 1
        dfs(calc_card(word_now, card_set))
        turn_now[i] -= 1
    # 마지막일때
    if last_turn:
        if word_now:
            possible_output.add(word_now)
        else:
            possible_output.add('EMPTY')
        return


def calc_card(word_now: str, card_set: list) -> str:
    for cmd, x in card_set:
        if cmd == 'ADD':
            word_now += x
        elif cmd == 'DEL':
            x = int(x)
            if x < 0 or x >= len(word_now):
                return 'ERROR'
            word_now = word_now[:x] + word_now[x + 1:]
    return word_now


n, c = map(int, input().split())
turn = []
for _ in range(n):
    _, *act = map(int, input().split())
    turn.append(act)

cards = [[]]
for _ in range(c):
    cards_list = list(input().strip().split(','))
    tmp = []
    for card in cards_list:
        tmp.append(tuple(card.split()))
    cards.append(tmp)


perm_list = []
for i in range(n):
    perm_list += [i] * len(turn[i])

possible_output = set()
turn_now = [0] * n

dfs('')
print(*sorted(possible_output), sep='\n')


'''
def dfs(word_now: str):
    global n, turn, cards, possible_output
    # 다음사람 카드 내는 것 탐색
    turn_left = False
    for i in range(n):
        # 더 낼수 있는 카드가 없다면
        if not turn[i]:
            continue
        # 아니라면 카드 내기
        turn_left = True
        # 다음 행동
        next_card = turn[i].pop()
        next_word = calc_card(word_now, cards[next_card])
        # ERROR 발생시 깊에 재귀 ㄴㄴ
        if next_word == 'ERROR':
            possible_output.add(next_word)
            continue
        dfs(next_word)
        turn[i].append(next_card)
    # 더 낼 수 있는 카드가 없다면
    if not turn_left:
        if not word_now:
            possible_output.add('EMPTY')
        else:
            possible_output.add(word_now)
        return


def calc_card(word_now: str, card_set: list) -> str:
    for c in card_set:
        cmd, x = c.split()
        if cmd == 'ADD':
            word_now += x
        elif cmd == 'DEL':
            x = int(x)
            if x < 0 or x >= len(word_now):
                return 'ERROR'
            word_now = word_now[:x] + word_now[x + 1:]
    return word_now


n, c = map(int, input().split())
turn = []
for _ in range(n):
    _, *act = map(int, input().split())
    turn.append(act[::-1])

cards = [()]
for _ in range(c):
    cards_list = list(input().strip().split(','))
    cards.append(cards_list)

possible_output = set()

dfs('')
print(*sorted(possible_output), sep='\n')
'''
