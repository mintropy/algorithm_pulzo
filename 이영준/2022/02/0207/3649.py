"""
Title : 로봇 프로젝트
Link : https://www.acmicpc.net/problem/3649
"""

import sys
input = sys.stdin.readline


while True:
    try:
        x = int(input()) * 10_000_000
        n = int(input())
        legos = sorted([int(input()) for _ in range(n)])
        
        possible = False
        left, right=  0, n - 1
        while left < right:
            lego_left, lego_right = legos[left], legos[right]
            if lego_right + lego_left == x:
                print(f'yes {lego_left} {lego_right}')
                possible = True
                break
            elif lego_right + lego_left < x:
                left += 1
            else:
                right -= 1
        if not possible:
            print('danger')
    except:
        break