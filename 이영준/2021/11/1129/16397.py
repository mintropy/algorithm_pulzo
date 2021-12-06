"""
Title : 탈출
Link : https://www.acmicpc.net/problem/16397
"""

from collections import deque
import sys
input = sys.stdin.readline

N, T, G = map(int, input().split())

visited = [100_000] * 100_000
queue = deque([(N, 0)])

while queue:
    num, button = queue.popleft()
    if button == T + 1:
        break
    if visited[num] <= button:
        continue
    visited[num] = button
    if num == G:
        break
    # push button
    if num < 99_999:
        queue.append((num + 1, button + 1))
    if 0 < num * 2 <= 99_999:
        queue.append((num * 2 - 10 ** (len(str(num * 2)) - 1), button + 1))

if visited[G] == 100_000:
    print('ANG')
else:
    print(visited[G])
