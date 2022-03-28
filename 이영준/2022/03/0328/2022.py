"""
Title : 사다리
Link : https://www.acmicpc.net/problem/2022
"""

from math import sqrt
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    X, Y, C = map(float, input().split())
    X2, Y2 = X * X, Y * Y
    left, right = 0, min(X, Y)
    ans = 0
    while right - left >= 1e-6:
        mid = (left + right) / 2
        mid2 = mid * mid
        h1, h2 = sqrt(X2 - mid2), sqrt(Y2 - mid2)
        if (h1 * h2) / (h1 + h2) <= C:
            ans = mid
            right = mid
        else:
            left = mid
    print(ans)

'''
참조 : https://burningjeong.tistory.com/307
'''
