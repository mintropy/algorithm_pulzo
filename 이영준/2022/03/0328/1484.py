"""
Title : 다이어트
Link : https://www.acmicpc.net/problem/1484
"""

import sys
input = sys.stdin.readline


def search(G) -> list:
    result = []
    st = end = 1
    while True:
        res = end * end - st * st
        if res == G:
            result.append(end)
            end += 1
        elif res < G:
            end += 1
        else:
            if end - st == 1:
                break
            st += 1
    return result


G = int(input())
result = search(G)
if result:
    print(*result, sep='\n')
else:
    print(-1)
