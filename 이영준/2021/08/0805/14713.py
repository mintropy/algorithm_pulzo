"""
Title : 앵무새
Link : https://www.acmicpc.net/problem/14713
"""

import sys
input = sys.stdin.readline


def search(parrots_idx: list, sentence_idx: int) -> bool:
    global n, parrots, sentence
    sentence_length = len(sentence)
    while True:
        if sentence_idx == len(sentence):
            break
        for i in range(len(parrots)):
            p_idx = parrots_idx[i]
            if p_idx >= len(parrots[i]):
                continue
            if sentence[sentence_idx] == parrots[i][p_idx]:
                sentence_length -= 1
                sentence_idx += 1
                parrots_idx[i] += 1
                break
        else:
            break
    
    parrot_empty = len(parrots)
    for i in range(len(parrots)):
        if parrots_idx[i] == len(parrots[i]):
            parrot_empty -= 1
    
    if not sentence_length and not parrot_empty:
        return True
    else:
        return False


n = int(input())
parrots = [list(map(str, input().split())) for _ in range(n)]
sentence = list(map(str, input().split()))

parrots_idx = [0] * len(parrots)
sentence_idx = 0


if search(parrots_idx, 0):
    print('Possible')
else:
    print('Impossible')



'''
# 효율 안좋은 풀이법
import sys
from typing import Deque
input = sys.stdin.readline

sys.setrecursionlimit(int(1e6))

def search(parrot_idx: list, idx: int) -> bool:
    global l, m, parrots, sentence, possible
    if idx == l:
        possible = True
        return
    
    for i in range(m):
        p_idx = parrot_idx[i]
        if p_idx >= len(parrots[i]):
            continue
        if parrots[i][p_idx] == sentence[idx]:
            parrot_idx[i] += 1
            search(parrot_idx, idx + 1)
            parrot_idx[i] -= 1


n = int(input())
parrots = [list(map(str, input().split())) for _ in range(n)]
sentence = list(map(str, input().split()))

l = len(sentence)
m = len(parrots)

parrot_idx = [False] * m

possible = False

search(parrot_idx, 0)

if possible:
    print('Possible')
else:
    print('Impossible')
'''