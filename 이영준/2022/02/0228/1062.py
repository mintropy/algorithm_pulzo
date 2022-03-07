"""
Title : 가르침
Link : https://www.acmicpc.net/problem/1062
"""

from itertools import combinations
import sys
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    alphabets = {'a', 'c', 'i', 'n', 't'}

    words = []
    additional_alphabests = set()
    for _ in range(N):
        word = input().strip()[4:-4]
        word = set(s for s in word) - alphabets
        words.append(word)
        additional_alphabests |= word

    limit = K - 5
    if limit < 0:
        print(0)
        return
    if len(list(additional_alphabests)) <= limit:
        ans = N
    else:
        ans = 0
        for comb in list(combinations(additional_alphabests, limit)):
            count = 0
            comb = set(comb)
            for word in words:
                for s in word:
                    if s not in comb:
                        break
                else:
                    count += 1
            if ans < count:
                ans = count
    print(ans)
    return


solution()
