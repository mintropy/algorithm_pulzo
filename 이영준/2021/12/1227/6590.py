"""
Title : 덧셈 체인
Link : https://www.acmicpc.net/problem/6590
"""

import sys
input = sys.stdin.readline


def dfs(target: int, now: list):
    global memory
    if now[-1] == target:
        memory[target] = now[::]
        return
    if len(now) >= len(memory[target]):
        return
    for i in range(len(now) - 1, -1, -1):
        for j in range(i + 1):
            tmp = now[i] + now[j]
            if tmp > target:
                break
            if tmp <= now[-1]:
                continue
            dfs(target, now + [now[i] + now[j]])


memory = [[0] * 100 for _ in range(101)]

for i in range(7):
    memory[2 ** i] = list(2 ** j for j in range(i + 1))
for i in range(3, 101):
    if len(memory[i]) != 100:
        continue
    last = memory[i - 1][::]
    while True:
        if last[-1] ** 2 > i:
            last.pop()
            dfs(i, last)
        else:
            break

while True:
    n = int(input())
    if n == 0:
        break
    print(*memory[n])
