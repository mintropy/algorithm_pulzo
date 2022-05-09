"""
Title : 균형
Link : https://www.acmicpc.net/problem/22968
"""

import sys
input = sys.stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    node_count = [0, 1]
    while node_count[-1] <= 1_000_000_000:
        node_count.append(node_count[-1] + node_count[-2] + 1)
    
    for _ in range(II()):
        V = II()
        for idx, count in enumerate(node_count):
            if count > V:
                print(idx - 1)
                break
