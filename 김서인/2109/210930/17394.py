import collections
import sys

input = sys.stdin.readline

T = int(input())

# 십만 이하 소수 구하기
primes = [True] * 100001
primes[0] = False
primes[1] = False

for i in range(2, 100001):
    if primes[i] == True:
        for j in range(i * 2, 100001, i):
            primes[j] = False


def sol():
    Q = collections.deque()
    visited[N] = True
    Q.append((N, 0))  # 현재 생명체의 수, 핑거 스냅 횟수

    while Q:
        life_cnt, finger_snap_cnt = Q.popleft()

        if life_cnt in target_primes:  # 목표 생명체 수이면
            return finger_snap_cnt

        finger_snap_results = [life_cnt // 2, life_cnt // 3, life_cnt + 1, life_cnt - 1]
        for finger_snap_result in finger_snap_results:
            if 0 <= finger_snap_result <= 1000000 and visited[finger_snap_result] == False:  # 범위 내, 방문 안 했으면
                visited[finger_snap_result] = True  # 방문 처리
                Q.append((finger_snap_result, finger_snap_cnt + 1))
    return -1


for tc in range(T):
    N, A, B = map(int, input().split())
    visited = [False] * 1000001

    target_primes = []
    for i in range(A, B + 1):
        if primes[i] == True:
            target_primes.append(i)

    # 범위 내에 소수가 없다면
    if len(target_primes) == 0:
        print(-1)
    else:  # 소수가 있다면
        ans = sol()
        print(ans)

print()