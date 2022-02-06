"""
Title : 자리수로 나누기
Link : https://www.acmicpc.net/problem/1490
"""

import sys
input = sys.stdin.readline


def find_num(pattern: int, nums: list) -> int:
    for i in range(10):
        base = pattern * (10 ** i)
        for additional in range(10 ** i):
            M = base + additional
            for num in nums:
                if M % num:
                    break
            else:
                return M


N = int(input())
nums = set(int(i) for i in str(N))
nums.discard(0)
print(find_num(N, nums))
