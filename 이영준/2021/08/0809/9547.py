"""
Title : 대통령 선거
Link : https://www.acmicpc.net/problem/9547
"""

import sys, collections
input = sys.stdin.readline


for tc in range(int(input())):
    c, v = map(int, input().split())
    preferance = [tuple(map(int, input().split())) for _ in range(v)]
    
    # c, v 가 1일 때
    if c == 1:
        print(1, 1)
        continue
    if v == 1:
        print(preferance[0][0], 1)
        continue
    
    candidate = collections.defaultdict(int)
    for i in range(v):
        candidate[preferance[i][0]] += 1
    
    cand_result = sorted(candidate.items(), key= lambda x: x[1], reverse= True)
    
    # 1차 투표에서 종료 가능한 경우
    if cand_result[0][1] > v // 2:
        print(cand_result[0][0], 1)
        continue
    
    cand1, cand2 = cand_result[0][0], cand_result[1][0]
    
    candidate = {cand1: 0, cand2: 0}
    for pref in preferance:
        for p in pref:
            if p == cand1:
                candidate[cand1] += 1
                break
            if p == cand2:
                candidate[cand2] += 1
                break
    
    v1, v2 = candidate[cand1], candidate[cand2]
    
    if v1 > v2:
        print(cand1, 2)
    else:
        print(cand2, 2)