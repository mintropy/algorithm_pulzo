import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
odd, even = 0, 0
for i in range(N):
    if i % 2 == 0:
        odd += cards[i]
    else:
        even += cards[i]
ans = odd
junghun = 0
for i in range(N - 1):
    if i % 2 == 0:
        # 밑장 뺀다
        ans = max(ans, junghun + even)
        # 안 뺀다
        junghun += cards[i]
    else:
        # 밑장 뺀다
        ans = max(ans, junghun + even - cards[-1])
        # 안 뺀다
        even -= cards[i]
print(ans)