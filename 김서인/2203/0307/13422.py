import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

T = int(input())
for _ in range(T):
    N, M, L = MIIS()
    houses = list(MIIS())

    ans = 0

    left, right = 0, M - 1
    stolen_money = sum(houses[left:right + 1])

    if N == M:
        if stolen_money < L:
            ans += 1
    else:

        while left < N:
            if stolen_money < L:
                ans += 1
            stolen_money -= houses[left]
            right += 1
            if right >= N:
                right = right - N
            stolen_money += houses[right]
            left += 1

    print(ans)
