import sys
input = sys.stdin.readline

PLAYER_COUNT = 3

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = list(range(N))
cnt = 0

while True:
    # 각 카드가 특정 플레이어에게 보내졌는지 확인
    for i in range(N):
        player = P[i]
        card_owner = cards.index(i) % PLAYER_COUNT
        if player != card_owner:
            break
    else:
        break

    # 카드 섞기
    new_cards = [0] * N
    for i in range(N):
        new_cards[S[i]] = cards[i]
    cards = new_cards

    # 카드 배치가 처음으로 돌아왔다면 불가능
    if cards == list(range(N)):
        cnt = -1
        break

    # cnt 증가
    cnt += 1

print(cnt)