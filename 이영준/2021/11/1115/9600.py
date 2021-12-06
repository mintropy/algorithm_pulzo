"""
Title : 돌 게임 6
Link : https://www.acmicpc.net/problem/9660
"""

import sys
input = sys.stdin.readline


N = int(input())
R = N % 7
print('CY' if (R == 0 or R == 2) else 'SK')
