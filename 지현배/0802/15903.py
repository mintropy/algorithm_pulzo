import sys
# 힙큐를 사용함
import heapq

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
heapq.heapify(cards)
# 우선 카드의 총합을 계산하고
total = sum(cards)
for _ in range(m):
    # 작은 카드 2개를 빼와서
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    # 2개를 더한 값을 2번 넣고
    heapq.heappush(cards, c1 + c2)
    heapq.heappush(cards, c1 + c2)
    # 총합에도 넣음
    total += c1 + c2
print(total)
