"""
Title : 카드 게임
Link : https://www.acmicpc.net/problem/10835
"""

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dfs(i: int, j: int) -> int:
    # 왼쪽 i카드, 오른쪽 j카드
    # 한 쪽 카드를 모두 사용했을 때
    if i == n or j == n:
        return 0
    # 이미 해당 칸에 도달했을 때
    # 모든 칸에서 최댓값을 저장하며 진행했으므로, 해당 값 반환
    if scores[i][j] >= 0:
        return scores[i][j]
    # 오른쪽 카드를 버리며 점수를 먹을 수 있을 때
    if left[i] > right[j]:
        scores[i][j] = dfs(i, j + 1) + right[j]
    # 왼쪽 카드, 왼쪽 + 오른쪽 카드를 버릴 때 점수
    # 순서대로 버리면서 더 큰 점수가 되기도 해서 모두 비교해야 되지만,
    # 어찌되었던 scores배열에 최댓값만 저장하면 되므로 상관 ㄴㄴ
    else:
        s1, s2 = dfs(i + 1, j), dfs(i + 1, j + 1)
        if s1 >= s2:
            scores[i][j] = s1
        else:
            scores[i][j] = s2
    return scores[i][j]


n = int(input())
left = list(MIIS())
right = list(MIIS())
scores = [[-1] * n for _ in range(n)]

print(dfs(0, 0))
