"""
Title : 우체국
Link : https://www.acmicpc.net/problem/2141
"""

import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    cities = sorted([tuple(map(int, input().split())) for _ in range(N)])
    now = cities[0][0]
    total_distance = right_total_people = 0
    for x, a in cities:
        total_distance += (x - now) * a
        right_total_people += a
    ans = cities[0][0]
    min_dist = total_distance
    left_total_people = 0
    for idx, (x, a) in enumerate(cities[1:]):
        diff = x - cities[idx][0]
        left_total_people += cities[idx][1]
        right_total_people -= cities[idx][1]
        total_distance += (left_total_people - right_total_people) * diff
        if min_dist > total_distance:
            min_dist = total_distance
            ans = x
    print(ans)
