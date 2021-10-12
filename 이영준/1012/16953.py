"""
Title : A → B
Link : https://www.acmicpc.net/problem/16953
"""

import collections
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
queue = collections.deque([(a, 1)])

ans = -1
while queue:
    x, c = queue.popleft()
    if x == b:
        ans = c 
        break
    if x * 2 <= b:
        queue.append((x * 2, c + 1))
    if x * 10 + 1 <= b:
        queue.append((x * 10 + 1, c + 1))

print(ans)
