"""
Title : 회문은 회문이아니야!!
Link : https://www.acmicpc.net/problem/15927
"""

import sys
input = sys.stdin.readline


def search(s):
    length = len(s)
    if s == s[0] * length:
        return -1
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return length
    return length - 1


s = input().strip()
print(search(s))
