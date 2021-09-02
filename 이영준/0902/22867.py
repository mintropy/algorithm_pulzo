"""
Title : 종점
Link : https://www.acmicpc.net/problem/22867
"""

import sys, heapq
input = sys.stdin.readline


n = int(input())
# HH:MM:SS.sss
schedual = []
for i in range(n):
    a, l = input().strip().split()
    a = a.replace(':', '')
    a = a.replace('.', '')
    l = l.replace(':', '')
    l = l.replace('.', '')
    schedual.append((a, l))

schedual.sort()
max_terminal = 1
terminal_now = 0
terminal = []
for a, l in schedual:
    if not terminal:
        heapq.heappush(terminal, l)
        terminal_now += 1
    else:
        if a >= terminal[0]:
            while terminal:
                if a >= terminal[0]:
                    heapq.heappop(terminal)
                    terminal_now -= 1
                else:
                    break
        heapq.heappush(terminal, l)
        terminal_now += 1
        if terminal_now > max_terminal:
            max_terminal = terminal_now

print(max_terminal)
