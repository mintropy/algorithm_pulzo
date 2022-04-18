"""
Title : 홍준 프로그래밍 대회
Link : https://www.acmicpc.net/problem/1222
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int (input())
    students = tuple(map(int ,input().split()))
    
    numbers = [0] * 2_000_001
    for student in students:
        numbers[student] += 1
    ans = 0
    for i in range(1, 2_000_001):
        count = sum(numbers[i:2_000_001:i])
        if count > 1 and ans < count * i:
            ans = count * i
    print(ans)
