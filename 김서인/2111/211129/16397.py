import collections
import sys

input = sys.stdin.readline

MIISS = lambda: map(int, input().strip().split())

# 최소로 버튼 눌러서 방 탈출 -> BFS

N, T, G = MIISS()
visited = set()


def sol():
    q = collections.deque()
    q.append((N, 0))
    visited.add(N)

    while q:
        num, cnt = q.popleft()

        if cnt > T: # 횟수 제한
            return 'ANG'

        if num == G: # 정답
            return cnt

        # A 버튼
        a_result = num + 1
        if 0<= a_result <= 99999 and a_result not in visited:

            q.append((a_result, cnt + 1))
            visited.add(a_result)

        if num == 0 : # 0이면 버튼 B 눌러도 수가 변하지 않음.
            continue

        # B 버튼
        b_tmp_result = (num * 2) # 2 곱하기

        if 0<= b_tmp_result <= 99999:
            b_result = b_tmp_result - (10 ** (len(str(b_tmp_result))-1)) # 0이 아닌 가장 높은 자릿수의 숫자가 1 줄어든다.
            # b_result = int(str(int(str(b_tmp_result)[0])- 1) + str(b_tmp_result)[1:])
            if b_result not in visited:
                q.append((b_result, cnt + 1))
                visited.add(b_result)

    return 'ANG'


ans = sol()
print(ans)