"""
Title : 암호 만들기
Link : https://www.acmicpc.net/problem/1759
"""

import sys, itertools
input = sys.stdin.readline

l, c = map(int, input().split())
comb = []

vowels = []
consonants = []
for alp in input().strip().split():
    if alp in {'a', 'e', 'i', 'o', 'u'}:
        vowels.append(alp)
    else:
        consonants.append(alp)

# 모음을 1개 이상 선택
for i in range(1, len(vowels) + 1):
    # 나머지를 자음으로 선택
    if l - i >= 2:
        vowels_porb = list(itertools.combinations(vowels, i))
        consonants_prob = list(itertools.combinations(consonants, l - i))
        comb.extend(list(itertools.product(vowels_porb, consonants_prob)))

output = []
for v, c in comb:
    tmp = [*v, *c]
    output.append(''.join(sorted(tmp)))

print(*sorted(output), sep='\n')
