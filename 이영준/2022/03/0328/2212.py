"""
Title : 센서
Link : https://www.acmicpc.net/problem/2212
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    sensors = sorted(set(map(int, input().split())))
    print(sum(sorted([sensors[i] - sensors[i - 1] for i in range(1, len(sensors))])[:len(sensors) - K]))
