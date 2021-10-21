import copy
import sys

input = sys.stdin.readline

def repetition_permutation(depth):
    if depth == C:
        orders.append(tuple(copy.copy(t)))
        return

    for i in range(N):
        if people_cards_cnt[i] > t[:depth].count(i): # 그 사람이 갖고 있는 카드 수보다 더 많이 X
            t[depth] = i
            repetition_permutation(depth + 1)

MIIS = lambda: map(int, input().split())
N, C = MIIS()

people_cards_cnt = []
# 카드 패(*번 사람이 가진 카드 패- 순서대로 내야 함)
people_cards = []
for _ in range(N):
    cards = tuple(MIIS())

    people_cards.append(cards[1:])
    people_cards_cnt.append(cards[0])

# 카드 명령 내용
card_order = dict()
for i in range(1, C + 1):
    tmp = input().strip().split(',')
    card_order[i] = tmp

# 그 결과
results = set()

# 어떤 순서로 진행하는지
orders = list()
t = [-1] * C
repetition_permutation(0)


# 위 순서로 진행해보기(안 되면 중간에 X)
for i in range(len(orders)):
    now_order = orders[i]
    now_str = []
    now_idx = [0]*N
    flag = True

    for order in now_order:  # 카드 하나씩 실행해보기

        now_commands = card_order[people_cards[order][now_idx[order]]]
        now_idx[order] += 1
        for com in now_commands:  # 카드 속 명령 모두 실행
            command, key = com.split()
            if flag == False:
                break

            if command == 'ADD':
                now_str.append(key)
            elif command == 'DEL':
                # 불가능하면 에러 처리
                if len(now_str) > int(key):
                    now_str.pop(int(key))
                else:
                    results.add('ERROR')
                    flag = False
                    break

    if flag == True: # 게임 끝까지 잘 마무리하고 종료된 건지 체크
        # 게임이 끝났을 때 빈 문자열이면 EMPTY
        if not now_str:
            results.add('EMPTY')
        # 그게 아니라면
        else:
            results.add(''.join(now_str))




results = sorted(list(results))
for result in results:
    print(result)
