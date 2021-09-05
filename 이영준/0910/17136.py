"""
Title : 색종이 붙이기
Link : https://www.acmicpc.net/problem/17136
"""

import sys
input = sys.stdin.readline


def dfs(pos):
    global count, colored_paper
    paper_used = 25 - sum(colored_paper)
    if pos == 100:
        if paper_used < count:
            count = paper_used
        return
    if paper_used > count:
        return
    # 색종이 크기 1~5 가능한지 & 놓기
    x, y = pos // 10, pos % 10
    for l in range(4, -1, -1):
        # 해당 범위가 가능한지
        if colored_paper[l + 1] and check(pos, l + 1):
            # 모두 덮기
            for i in range(x, x + l + 1):
                for j in range(y, y + l + 1):
                    paper[i][j] = 0
            colored_paper[l + 1] -= 1
            # 재귀
            dfs(find_next(pos + 1))
            # 덮은거 치우기
            for i in range(x, x + l + 1):
                for j in range(y, y + l + 1):
                    paper[i][j] = 1
            colored_paper[l + 1] += 1


def find_next(pos: int) -> int:
    global paper
    while True:
        if pos == 100:
            return pos
        x, y = pos // 10, pos % 10
        if paper[x][y]:
            return pos
        pos += 1


def check(pos: int, lenght: int) -> bool:
    global paper
    x, y = pos // 10, pos % 10
    if x + lenght - 1 >= 10 or y + lenght - 1 >= 10:
        return False
    for i in range(x, x + lenght):
        for j in range(y, y + lenght):
            if not paper[i][j]:
                return False
    return True


paper = [list(map(int, input().split())) for _ in range(10)]
# 색종이
colored_paper = [5] * 5

count = 26
dfs(find_next(0))

if count == 26:
    print(-1)
else:
    print(count)
