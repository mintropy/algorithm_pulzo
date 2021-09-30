import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

import itertools

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

max_joy = 0
for case in powerset(range(N)):
    hp = 100
    joy = 0
    for i in case:
        hp -= L[i]
        if hp < 1:
            break
        joy += J[i]
    max_joy = max(max_joy, joy)

print(max_joy)