"""
Title : 판치기
Link : https://www.acmicpc.net/problem/23085
"""

import collections


def bfs(n, k, back):
    queue = collections.deque([(back, 0)])
    # 뒷면 카드 개수
    check = [False] * (n + 1)
    while queue:
        b, c = queue.popleft()
        f = n - b
        # 탐색 완료
        if b == n:
            return c
        if check[b]:
            continue
        check[b] = True
        # k-뒤집기 실행
        for i in range(k + 1):
            # 앞면을 i개, 뒷면을 k - i개 뒤집기
            if f >= i and b >= k - i and not check[b + (2 * i - k)]:
                queue.append((b + (2 * i - k), c + 1))
    return -1


n, k = map(int, input().split())
coins = input().strip()
back = coins.count('T')

print(bfs(n, k, back))
