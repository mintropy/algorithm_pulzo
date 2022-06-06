"""
Title : 입국심사
Link : https://www.acmicpc.net/problem/3079
"""

import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    times = [int(input()) for _ in range(N)]
    left, right = 1, 10 ** 18
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        max_count = sum([mid // time for time in times])
        if max_count >= M:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
