"""
Title : 문자열 복사
Link : https://www.acmicpc.net/problem/2195
"""

import sys
input = sys.stdin.readline


S = input().strip()
P = input().strip()

alp_idx_dict = {}
for idx, s in enumerate(S):
    alp_idx_dict[s] = alp_idx_dict.get(s, []) + [idx]

idx = 0
copy_function = 0
length_S = len(S)
length_P = len(P)

while idx < length_P:
    alp_list = alp_idx_dict[P[idx]]
    count = 0
    
    for alp_idx in alp_list:
        tmp_count = 0
        p_idx = idx
        while alp_idx < length_S and p_idx < length_P:
            if S[alp_idx] == P[p_idx]:
                alp_idx += 1
                p_idx += 1
                tmp_count += 1
            else:
                break
        if tmp_count > count:
            count = tmp_count
    
    copy_function += 1
    idx += count

print(copy_function)
