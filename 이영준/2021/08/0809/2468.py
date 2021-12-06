"""
Title : 안전 영역
Link : https://www.acmicpc.net/problem/2468
"""

import sys, collections
n = int(input())
heights = [list(map(int, input().split())) for _ in range(n)]

max_area = 0

direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

for h in range(0, 100 + 1):
    count = [[False] * n for _ in range(n)]
    area = 0
    for i in range(n):
        for j in range(n):
            if count[i][j]:
                continue
            if heights[i][j] <= h:
                continue
            area += 1
            queue = collections.deque([(i, j)])
            count[i][j] = True
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    d = direction[k]
                    x2, y2 = x + d[0], y + d[1]
                    if x2 < 0 or x2 >= n:
                        continue
                    if y2 < 0 or y2 >= n:
                        continue
                    if count[x2][y2]:
                        continue
                    if heights[x2][y2] <= h:
                        continue
                    queue.append((x2, y2))
                    count[x2][y2] = True
    
    if area == 0:
        break
    if area > max_area:
        max_area = area

print(max_area)