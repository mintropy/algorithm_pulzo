"""
Title : 경로 게임
Link : https://www.acmicpc.net/problem/12887
"""

import sys
input = sys.stdin.readline

M = int(input())
paths = [input().strip() for _ in range(2)]

count = 0
last_black = -1
for i in range(M):
    if paths[0][i] == '#' or paths[1][i] == '#':
        if last_black == -1:
            count += i
        else:
            if paths[0][last_black] == paths[0][i]:
                count += (i - last_black) - 1
            else:
                count += (i - last_black) - 2
        last_black = i
else:
    count += (M - last_black)- 1

print(count)
