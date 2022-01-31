"""
Title : 화살을 쏘자!
Link : https://www.acmicpc.net/problem/20157
"""

from collections import defaultdict
from math import gcd
import sys
input = sys.stdin.readline


N = int(input())

sector = {(True, True): 1, (False, True): 2, (False, False): 3, (True, False): 4}
bloons = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        if y > 0:
            bloons['x+'] += 1
        else:
            bloons['x-'] += 1
        continue
    if y == 0:
        if x > 0:
            bloons['y+'] += 1
        else:
            bloons['y-'] += 1
    g = gcd(x, y)
    x, y = x // g, y // g
    s = sector[(x > 0, y > 0)]
    if x < 0:
        x, y = -x, -y
    bloons[(s, x, y)] += 1

print(max(bloons.values()))
