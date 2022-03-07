"""
Title : 걷는 건 귀찮아
Link : https://www.acmicpc.net/problem/20928
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int , input().split())


if __name__ == '__main__':
    N, M = MIIS()
    positions = list(MIIS())
    moves = list(MIIS())

    min_count = N + 1
    count = [-1] * (N + 1)
    count[0] = 0
    right = 0
    for left, pos in enumerate(positions):
        if count[left] == -1:
            break
        max_range = moves[left]
        if M <= pos + max_range:
            count[-1] = count[left]
            break
        for i in range(right + 1, N):
            next_pos = positions[i]
            if next_pos > pos + max_range:
                break
            count[i] = count[left] + 1
            right = i
    print(count[-1])

'''
Counter Example
4 10
1 3 5 7
4 6 5 2

1 1
1
1

5 20
1 4 8 12 16
5 8 2 7 4
'''
