"""
Title : 가장높은탑쌓기
Link : https://www.acmicpc.net/problem/2655
"""

import sys
input = sys.stdin.readline

n = int(input())
# 밑면 너비, 높이, 무게
# 밑면 너비 오름차순 정렬
blocks = []
for i in range(n):
    blocks.append((i, tuple(map(int, input().split()))))
blocks.sort(key=lambda x:-x[1][0])

# 해당 블록을 쌓았을 때 높이
dp = [0] * n

# 가장 높은 경우 탐색
max_height = dp[0]
max_height_idx = 0
for i in range(n):
    idx, (_, h1, w1) = blocks[i]
    dp[i] = h1
    # 더 위에 둘 수 있는 블록 탐색
    for j in range(i):
        h2, w2 = dp[j], blocks[j][1][2]
        # j번째 블록이 더 무겁고, 합쳐서 쌓은 높이가 더 높은 경우
        if w2 > w1 and h2 + h1 > dp[i]:
            dp[i] = h2 + h1
    if dp[i] > max_height:
        max_height = dp[i]
        max_height_idx = i

# 그럴 경우 해당하는 블록 찾기
ans = []
for i in range(max_height_idx, -1, -1):
    if dp[i] == max_height:
        ans.append(blocks[i][0] + 1)
        max_height -= blocks[i][1][1]
    elif max_height == 0:
        break

print(len(ans))
print(*ans, sep='\n')


'''
5
1 5 1
25 3 5
9 2 3
16 6 7
4 4 5
'''