"""
Title : 전설의 JBNU
Link : https://www.acmicpc.net/problem/12757
"""

import bisect
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bin_search(keys, key):
    global K
    idx = bisect.bisect(keys, key)
    if idx == 0:
        if abs(keys[0] - key) <= K:
            return keys[0]
    elif idx == len(keys):
        if abs(keys[idx - 1] - key) <= K:
            return keys[idx - 1]
    else:
        if keys[idx] - key == key - keys[idx - 1]:
            return -2
        elif keys[idx] - key > key - keys[idx - 1]:
            if key - keys[idx - 1] <= K:
                return keys[idx - 1]
        else:
            if keys[idx] - key <= K:
                return keys[idx]
    return -1


if __name__ == "__main__":
    N, M, K = MIIS()
    data = {}
    keys = []
    for _ in range(N):
        k, v = MIIS()
        data[k] = v
        bisect.insort(keys, k)
    for _ in range(M):
        cmd, *kv = list(MIIS())
        if cmd == 1:
            k, v = kv
            data[k] = v
            bisect.insort(keys, k)
        elif cmd == 2:
            k, v = kv
            key = bin_search(keys, k)
            if key <= -1:
                continue
            data[key] = v
        else:
            k = kv[0]
            if k in data:
                print(data[k])
            else:
                ans = bin_search(keys, k)
                if ans == -1:
                    print(ans)
                elif ans == -2:
                    print("?")
                else:
                    print(data[ans])
