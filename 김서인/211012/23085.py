import collections
import sys

input = sys.stdin.readline


def bfs(back_cnt):
    visited = [0] * (N + 1)  # 뒤집힌 동전이 몇 개인지

    q = collections.deque()
    q.append((back_cnt, 0))  # 뒤집힌 동전의 개수, 몇 번 K-뒤집기 사용했는지

    while q:
        tmp_back_cnt, k_turn_cnt = q.popleft()
        tmp_front_cnt = N - tmp_back_cnt
        if tmp_back_cnt == N:
            return k_turn_cnt

        if visited[tmp_back_cnt]:  # 이미 이 동전 개수일 때 K-뒤집기한 적이 있으면 더 이상 하지 않기
            continue

        visited[tmp_back_cnt] = 1

        for i in range(K + 1):  # 0~K개의 뒷면인 동전 뒤집기
            turn_back = i  # 뒷면인 동전 뒤집을 개수
            turn_front = K - i  # 앞면인 동전 뒤집을 개수

            if turn_back > tmp_back_cnt or turn_front > tmp_front_cnt:  # 뒤집힐 수 있는 개수보다 뒤집을 개수가 클 수는 없음
                continue

            back_cnt = tmp_back_cnt - turn_back + turn_front
            if N >= back_cnt >= 0 :
                q.append((back_cnt, k_turn_cnt + 1))

    return -1


N, K = map(int, input().strip().split())
S = input().strip()

back_cnt = 0
# 초기 상태 세팅
for i in range(N):
    if S[i] == 'T':
        back_cnt += 1


ans = bfs(back_cnt)
print(ans)
