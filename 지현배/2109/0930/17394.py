import sys
from collections import deque
input = sys.stdin.readline
def sol():
    N, A, B = map(int, input().split())
    # B 이하 소수를 모두 구한다.
    primes = [2]
    for n in range(3, B + 1, 2):
        i = 0
        while i < len(primes) and primes[i] < n ** 0.5 + 1:
            if n % primes[i] == 0:
                break
            i += 1
        else:
            primes.append(n)
    # A 이상으로 필터링
    primes = list(filter(lambda x: x >= A, primes))
    if len(primes) == 0:
        return -1
    # 스냅으로 인구 증가는 1씩 증가가 유일하므로
    # N이 A보다 작은 경우 가장 작은 소수와의 차를 구한다.
    if N <= A:
        return primes[0] - N
    else:
        visited = [0] * (N // 32 + 10)
        queue = deque([[N, 0]])
        while queue:
            n, cnt = queue.popleft()
            if n in primes:
                return cnt
            visited[n // 32] |= 1 << (n % 32)
            if primes[0] <= n:
                if not (visited[(n // 3) // 32] & (1 << ((n // 3) % 32))):
                    queue.append([n // 3, cnt + 1])
                if not (visited[(n // 2) // 32] & (1 << ((n // 2) % 32))):
                    queue.append([n // 2, cnt + 1])
                if not (visited[(n - 1) // 32] & (1 << ((n - 1) % 32))):
                    queue.append([n - 1, cnt + 1])
            if 0 <= n <= primes[-1]:
                if not (visited[(n + 1) // 32] & (1 << ((n + 1) % 32))):
                    queue.append([n + 1, cnt + 1])
T = int(input())
for _ in range(T):
    print(sol())