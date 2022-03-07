"""
Title : 세 용액
Link : https://www.acmicpc.net/problem/2473
"""

import sys
input = sys.stdin.readline


def two_pointer(N: int, feature: list) -> tuple:
    ans = (feature[0], feature[1], feature[2])
    for _ in range(N - 2):
        num = feature.pop()
        left, right = 0, len(feature) - 1
        for _ in range(len(feature) - 1):
            sum_feacher = num + feature[left] + feature[right]
            if abs(sum(ans)) > abs(sum_feacher):
                ans = (feature[left], feature[right], num)
            if sum_feacher < 0:
                left += 1
            else:
                right -= 1
        if sum(ans) == 0:
            break
    return ans


if __name__ == '__main__':
    N = int(input())
    feature = sorted(map(int, input().split()))
    
    if feature[0] >= 0:
        print(*feature[:3])
    elif feature[-1] <= 0:
        print(*feature[-3:])
    else:
        print(*two_pointer(N, feature))

'''
Counter Example
7
912022275 -968846127 195376182 -212509759 589371385 817446019 -59843192

output : -968846127-59843192+817446019 = -211243300
ans : -968846127+195376182+817446019 = 43976074
'''