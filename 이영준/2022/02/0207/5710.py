"""
Title : 전기 요금
Link : https://www.acmicpc.net/problem/5710
"""

import sys
input = sys.stdin.readline


def bin_search(total_usage: int, diff: int) -> int:
    min_usage, max_usage = 0, total_usage // 2
    while min_usage <= max_usage:
        mid_useage = (min_usage + max_usage) // 2
        other_usage = total_usage - mid_useage
        sk_fee = calculate_fee(mid_useage)
        other_fee = calculate_fee(other_usage)
        if other_fee - sk_fee == diff:
            return sk_fee
        elif other_fee - sk_fee > diff:
            min_usage = mid_useage + 1
        else:
            max_usage = mid_useage - 1


def calculate_total_usage(fee: int) -> int:
    if fee <= 200:
        return fee // 2
    elif fee <= 29900 + 200:
        return (fee - 200) // 3 + 100
    elif fee <= 4_979_900 + 29900 + 200:
        return (fee - 29900) // 5 + 100 + 9900
    else:
        return (fee - 4_979_900) // 7 + 100 + 9900 + 990_000


def calculate_fee(use: int) -> int:
    fee = 0
    if use > 1_000_000:
        fee += (use - 1_000_000) * 7
        use = 1_000_000
    if use > 10000:
        fee += (use - 10000) * 5
        use = 10000
    if use > 100:
        fee += (use - 100) * 3
        use = 100
    fee += use * 2
    return fee


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    total_usage = calculate_total_usage(A)
    print(bin_search(total_usage, B))
