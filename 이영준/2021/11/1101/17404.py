"""
Title : RBG거리 2
Link : https://www.acmicpc.net/problem/17404
"""

import sys
input = sys.stdin.readline


n = int(input())
RGB = [tuple(map(int, input().split())) for _ in range(n)]

# n == 2이면 경우의 수는 6가지
if n == 2:
    print(min((RGB[0][0] + RGB[1][1], RGB[0][0] + RGB[1][2],\
               RGB[0][1] + RGB[1][0], RGB[0][1] + RGB[1][2],\
               RGB[0][2] + RGB[1][0], RGB[0][2] + RGB[1][1])))
else:
    # 기초작업
    # XY이면 처음 X에서 시작, 지금 Y일때 최솟값
    RR = RG = RB = RGB[0][0]
    RR += min(RGB[1][1], RGB[1][2]) + RGB[2][0]
    RG += RGB[1][2] + RGB[2][1]
    RB += RGB[1][1] + RGB[2][2]
    GR = GG = GB = RGB[0][1]
    GG += min(RGB[1][0], RGB[1][2]) + RGB[2][1]
    GR += RGB[1][2] + RGB[2][0]
    GB += RGB[1][0] + RGB[2][2]
    BR = BG = BB = RGB[0][2]
    BB += min(RGB[1][0], RGB[1][1]) + RGB[2][2]
    BR += RGB[1][1] + RGB[2][0]
    BG += RGB[1][0] + RGB[2][1]
    # 값 계산
    for i in range(3, n):
        RR, RG, RB = min(RG + RGB[i][0], RB + RGB[i][0]),\
                     min(RR + RGB[i][1], RB + RGB[i][1]),\
                     min(RR + RGB[i][2], RG + RGB[i][2])
        GR, GG, GB = min(GG + RGB[i][0], GB + RGB[i][0]),\
                     min(GR + RGB[i][1], GB + RGB[i][1]),\
                     min(GR + RGB[i][2], GG + RGB[i][2])
        BR, BG, BB = min(BG + RGB[i][0], BB + RGB[i][0]),\
                     min(BR + RGB[i][1], BB + RGB[i][1]),\
                     min(BR + RGB[i][2], BG + RGB[i][2])
    print(min((RG, RB, GR, GB, BR, BG)))
