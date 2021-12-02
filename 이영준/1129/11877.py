"""
Title : 홍수
Link : https://www.acmicpc.net/problem/11877
"""

import sys
input = sys.stdin.readline


N, X = map(int, input().split())

if X > (N * N - 3 * N + 2) // 2:
    print(-1)
else:
    output = [N]
    rest = []
    left_volumn = X
    for i in range(1, N - 1):
        if (N - 1) - i > left_volumn:
            rest.append(i)
        else:
            output.append(i)
            left_volumn -= (N - 1) - i
    output = rest + output + [N - 1]
    print(*output)
