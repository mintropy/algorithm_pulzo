"""
title : 되돌리기
Link : https://www.acmicpc.net/problem/1360
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    editor = ""
    results = []
    for _ in range(int(input())):
        cmd, x, y = input().strip().split()
        if cmd == "type":
            editor += x
            results.append((int(y), editor))
        else:
            x, y = int(x), int(y)
            undos = []
            for time, text in results[::-1]:
                if time >= y - x:
                    continue
                editor = text
                break
            else:
                editor = ""
            results.append((y, editor))
    print(results[-1][1])
