from time import sleep
from collections import deque
from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

L, C = map(int, input().split())
S = sorted(input().rstrip().split())


def dfs(pos, n, con1, con2, l):
    if n == L:
        if con1 >= 1 and con2 >= 2:
            print(''.join(l))

    for i in range(pos, C):
        l.append(S[i])
        if S[i] in 'aeiou':
            con1 += 1
        else:
            con2 += 1
        dfs(i+1, n+1, con1, con2, l)
        if S[i] in 'aeiou':
            con1 -= 1
        else:
            con2 -= 1
        l.pop()


dfs(0, 0, 0, 0, [])
